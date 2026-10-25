from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import lru_cache
from http import HTTPStatus
from string import Formatter
from typing import Any, cast
from urllib.parse import quote

from pydantic import TypeAdapter, ValidationError

from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.exceptions.api import create_api_error
from aiohh.exceptions.decode import ClientDecodeError
from aiohh.methods.base import BaseMethod, ReturningType

DEFAULT_API_URL = "https://api.hh.ru"
DEFAULT_TIMEOUT = 60.0

QUERY_FIELDS = frozenset({"host", "locale"})
BODY_HTTP_METHODS = frozenset({HTTPMethod.POST, HTTPMethod.PUT})


@dataclass(frozen=True)
class Request:
    http_method: HTTPMethod
    url: str
    headers: dict[str, str] = field(default_factory=dict)
    params: list[tuple[str, str]] = field(default_factory=list)
    json: Any = None
    data: list[tuple[str, str]] | None = None


@dataclass(frozen=True)
class Response:
    status_code: int
    content: bytes


@lru_cache
def get_type_adapter(returning: Any) -> TypeAdapter[Any]:
    return TypeAdapter(returning)


def get_endpoint_fields(endpoint: str) -> set[str]:
    return {name for _, name, _, _ in Formatter().parse(endpoint) if name}


def encode_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"

    return str(value)


def encode_params(values: dict[str, Any]) -> list[tuple[str, str]]:
    params = []

    for name, value in values.items():
        for item in value if isinstance(value, list) else [value]:
            if isinstance(item, dict):
                params.extend(encode_params(item))
            else:
                params.append((name, encode_value(item)))

    return params


class BaseSession(ABC):
    def __init__(
        self, api_url: str = DEFAULT_API_URL, timeout: float = DEFAULT_TIMEOUT
    ) -> None:
        self.api_url = api_url.rstrip("/")
        self.timeout = timeout

    async def __call__(
        self, method: BaseMethod[ReturningType], headers: dict[str, str]
    ) -> ReturningType:
        request = self.build_request(method=method, headers=headers)
        response = await self.send(request)

        return self.parse_response(method=method, response=response)

    @abstractmethod
    async def send(self, request: Request) -> Response:
        raise NotImplementedError

    @abstractmethod
    async def close(self) -> None:
        raise NotImplementedError

    def build_request(
        self, method: BaseMethod[Any], headers: dict[str, str]
    ) -> Request:
        values = method.model_dump(mode="json", by_alias=True, exclude_none=True)
        endpoint_fields = get_endpoint_fields(method.__endpoint__)

        endpoint = method.__endpoint__.format(
            **{name: quote(str(values.pop(name)), safe="") for name in endpoint_fields}
        )

        if method.__http_method__ not in BODY_HTTP_METHODS:
            return Request(
                http_method=method.__http_method__,
                url=f"{self.api_url}{endpoint}",
                headers=headers,
                params=encode_params(values),
            )

        query_fields = QUERY_FIELDS | method.__query__
        query = {name: value for name, value in values.items() if name in query_fields}
        body = {
            name: value for name, value in values.items() if name not in query_fields
        }

        if method.__body_format__ is BodyFormat.FORM:
            return Request(
                http_method=method.__http_method__,
                url=f"{self.api_url}{endpoint}",
                headers=headers,
                params=encode_params(query),
                data=encode_params(body),
            )

        return Request(
            http_method=method.__http_method__,
            url=f"{self.api_url}{endpoint}",
            headers=headers,
            params=encode_params(query),
            json=body,
        )

    def parse_response(
        self, method: BaseMethod[ReturningType], response: Response
    ) -> ReturningType:
        if not HTTPStatus.OK <= response.status_code < HTTPStatus.MULTIPLE_CHOICES:
            raise create_api_error(
                method=method,
                status_code=response.status_code,
                content=response.content,
            )

        if method.__returning__ is None:
            return cast(ReturningType, None)

        try:
            result = get_type_adapter(method.__returning__).validate_json(
                response.content
            )
        except ValidationError as error:
            raise ClientDecodeError(
                f"Failed to decode response of {type(method).__name__}: {error}"
            ) from error

        return cast(ReturningType, result)
