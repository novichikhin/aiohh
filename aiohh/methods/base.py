from abc import ABC
from typing import Generic, TypeVar, ClassVar

from pydantic import (
    BaseModel,
    ConfigDict,
    Extra
)

from aiohh.types.base import BaseType

ReturningType = TypeVar("ReturningType", bound=BaseType)


class BaseMethod(ABC, BaseModel, Generic[ReturningType]):
    model_config = ConfigDict(extra=Extra.allow, frozen=True)

    __returning__: ClassVar[type]

    url: ClassVar[str]
    http_method: ClassVar[str]
