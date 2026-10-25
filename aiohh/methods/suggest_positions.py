from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.suggests import PositionSuggest


class SuggestPositions(BaseMethod[Items[PositionSuggest]]):
    __returning__ = Items[PositionSuggest]
    __endpoint__ = "/suggests/positions"

    text: str
