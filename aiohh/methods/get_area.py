from typing import Literal

from aiohh.methods.base import BaseMethod
from aiohh.types.area import Area


class GetArea(BaseMethod[Area]):
    __returning__ = Area
    __endpoint__ = "/areas/{area_id}"

    area_id: int | str
    additional_case: Literal["prepositional"] | None = None
