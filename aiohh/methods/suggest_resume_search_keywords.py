from aiohh.methods.base import BaseMethod
from aiohh.types.suggests import KeywordSuggests


class SuggestResumeSearchKeywords(BaseMethod[KeywordSuggests]):
    __returning__ = KeywordSuggests
    __endpoint__ = "/suggests/resume_search_keyword"

    text: str
