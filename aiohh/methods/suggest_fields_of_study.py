from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.suggests import FieldOfStudySuggest


class SuggestFieldsOfStudy(BaseMethod[Items[FieldOfStudySuggest]]):
    __returning__ = Items[FieldOfStudySuggest]
    __endpoint__ = "/suggests/fields_of_study"

    text: str
