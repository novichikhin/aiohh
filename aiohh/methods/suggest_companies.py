from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.suggests import CompanySuggest


class SuggestCompanies(BaseMethod[Items[CompanySuggest]]):
    __returning__ = Items[CompanySuggest]
    __endpoint__ = "/suggests/companies"

    text: str
