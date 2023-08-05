from abc import ABC

from pydantic import (
    BaseModel,
    ConfigDict,
    Extra
)


class BaseType(ABC, BaseModel):
    model_config = ConfigDict(extra=Extra.allow, frozen=True)
