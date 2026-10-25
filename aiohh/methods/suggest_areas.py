from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.suggests import AreaSuggest


class SuggestAreas(BaseMethod[Items[AreaSuggest]]):
    __returning__ = Items[AreaSuggest]
    __endpoint__ = "/suggests/areas"

    text: str
    area_id: int | str | None = None
    include_parent: bool | None = None
