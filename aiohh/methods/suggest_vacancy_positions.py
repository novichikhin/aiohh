from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.suggests import VacancyPositionSuggest


class SuggestVacancyPositions(BaseMethod[Items[VacancyPositionSuggest]]):
    __returning__ = Items[VacancyPositionSuggest]
    __endpoint__ = "/suggests/vacancy_positions"

    text: str
