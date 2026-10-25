import json
from http import HTTPStatus
from typing import Any

from pydantic import BaseModel, ConfigDict, ValidationError

from aiohh.exceptions.base import AiohhError
from aiohh.methods.base import BaseMethod


class ErrorDetail(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    type: str
    value: str | None = None


class APIError(AiohhError):
    def __init__(
        self,
        *,
        method: BaseMethod[Any],
        status_code: int,
        errors: list[ErrorDetail],
        description: str | None = None,
        request_id: str | None = None,
        oauth_error: str | None = None,
    ) -> None:
        self.method = method
        self.status_code = status_code
        self.errors = errors
        self.description = description
        self.request_id = request_id
        self.oauth_error = oauth_error

        super().__init__(self.build_message())

    def build_message(self) -> str:
        details = ", ".join(
            f"{error.type}={error.value}" if error.value else error.type
            for error in self.errors
        )
        parts = [
            f"{type(self.method).__name__} failed with status {self.status_code}",
            details,
            self.description,
            self.request_id and f"request_id={self.request_id}",
        ]

        return ": ".join(part for part in parts if part)

    def has_error(self, error_type: str, value: str | None = None) -> bool:
        return any(
            error.type == error_type and (value is None or error.value == value)
            for error in self.errors
        )


class BadRequestError(APIError):
    pass


class UnauthorizedError(APIError):
    pass


class ForbiddenError(APIError):
    @property
    def captcha_url(self) -> str | None:
        for error in self.errors:
            if error.type == "captcha_required":
                return getattr(error, "captcha_url", None)

        return None


class NotFoundError(APIError):
    pass


class ConflictError(APIError):
    pass


class TooManyRequestsError(APIError):
    pass


class ServerError(APIError):
    pass


ERRORS_BY_STATUS: dict[int, type[APIError]] = {
    HTTPStatus.BAD_REQUEST: BadRequestError,
    HTTPStatus.UNAUTHORIZED: UnauthorizedError,
    HTTPStatus.FORBIDDEN: ForbiddenError,
    HTTPStatus.NOT_FOUND: NotFoundError,
    HTTPStatus.CONFLICT: ConflictError,
    HTTPStatus.TOO_MANY_REQUESTS: TooManyRequestsError,
}


def create_api_error(
    method: BaseMethod[Any], status_code: int, content: bytes
) -> APIError:
    try:
        payload = json.loads(content)
    except ValueError:
        payload = None

    if not isinstance(payload, dict):
        payload = {}

    if "error" in payload:
        raw_errors = [
            {"type": payload["error"], "value": payload.get("error_description")}
        ]
    else:
        raw_errors = payload.get("errors") or []

    try:
        errors = [ErrorDetail.model_validate(error) for error in raw_errors]
    except ValidationError:
        errors = []

    error_class: type[APIError]

    if status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
        error_class = ServerError
    else:
        error_class = ERRORS_BY_STATUS.get(status_code, APIError)

    return error_class(
        method=method,
        status_code=status_code,
        errors=errors,
        description=payload.get("description"),
        request_id=payload.get("request_id"),
        oauth_error=payload.get("oauth_error"),
    )
