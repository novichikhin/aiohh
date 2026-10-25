from typing import Any, ClassVar, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

from aiohh.enums.body_format import BodyFormat
from aiohh.enums.host import Host
from aiohh.enums.http_method import HTTPMethod

ReturningType = TypeVar("ReturningType")


class BaseMethod(BaseModel, Generic[ReturningType]):
    model_config = ConfigDict(frozen=True, extra="forbid", validate_by_name=True)

    __returning__: ClassVar[Any]
    __http_method__: ClassVar[HTTPMethod] = HTTPMethod.GET
    __endpoint__: ClassVar[str]
    __body_format__: ClassVar[BodyFormat] = BodyFormat.JSON
    __query__: ClassVar[frozenset[str]] = frozenset()
    __authorized__: ClassVar[bool] = True

    host: Host | None = None
    locale: str | None = None
