import json
from abc import ABC, abstractmethod
from http import HTTPStatus
from typing import (
    Generic,
    TypeVar,
    Any,
    Optional,
    Dict,
    cast,
    Mapping
)

from pydantic import BaseModel, ConfigDict

from aiohh.exceptions.api import APIError
from aiohh.exceptions.decode import ClientDecodeError
from aiohh.methods.base import BaseMethod, ReturningType

Session = TypeVar("Session", bound=Any)


class Request(BaseModel):
    model_config = ConfigDict(frozen=True)

    url: str
    http_method: str

    params: Optional[Dict[str, Any]] = None
    body: Optional[Dict[str, Any]] = None
    headers: Dict[str, Any] = {}


class Response(BaseModel):
    model_config = ConfigDict(frozen=True)

    status_code: int
    body: bytes
    headers: Mapping[str, Any]
    content_type: str


class BaseSession(ABC, Generic[Session]):

    def __init__(self):
        self._session: Optional[Session] = None

    def _build_request(
            self,
            method: BaseMethod[ReturningType],
            headers: Mapping[str, Any]
    ) -> Request:
        dumped_model = method.model_dump()

        params = dumped_model if method.http_method == "GET" else None

        return Request(
            url=method.url.format(**dumped_model),
            http_method=method.http_method,
            params=params,
            body=params or dumped_model,
            headers=headers
        )

    def _build_response(
            self,
            status_code: int,
            body: bytes,
            headers: Mapping[str, Any],
            content_type: str
    ) -> Response:
        return Response(
            status_code=status_code,
            body=body,
            headers=headers,
            content_type=content_type
        )

    def _parse_response(
            self,
            method: BaseMethod[ReturningType],
            response: Response
    ) -> ReturningType:
        try:
            content = cast(Dict[str, Any], json.loads(response.body))
        except json.JSONDecodeError:
            raise ClientDecodeError

        if HTTPStatus.OK <= response.status_code <= HTTPStatus.IM_USED:
            return cast(
                ReturningType,
                method.__returning__.model_validate(content)  # type: ignore
            )

        raise APIError(
            method=method,
            status_code=response.status_code,
            detailed_errors=content.get("errors", [])
        )

    async def __call__(
            self,
            method: BaseMethod[ReturningType],
            headers: Mapping[str, Any]
    ) -> ReturningType:
        raise NotImplementedError

    @abstractmethod
    def create(self) -> Session:
        raise NotImplementedError

    @abstractmethod
    async def close(self) -> None:
        raise NotImplementedError
