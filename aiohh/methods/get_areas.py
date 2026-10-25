from typing import Literal

from aiohh.methods.base import BaseMethod
from aiohh.types.area import Area


class GetAreas(BaseMethod[list[Area]]):
    __returning__ = list[Area]
    __endpoint__ = "/areas"

    additional_case: Literal["prepositional"] | None = None
