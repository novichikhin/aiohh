from aiohh.methods.base import BaseMethod
from aiohh.types.suggests import KeywordSuggests


class SuggestVacancySearchKeywords(BaseMethod[KeywordSuggests]):
    __returning__ = KeywordSuggests
    __endpoint__ = "/suggests/vacancy_search_keyword"

    text: str
