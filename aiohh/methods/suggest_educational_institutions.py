from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.dictionaries import EducationalInstitution


class SuggestEducationalInstitutions(BaseMethod[Items[EducationalInstitution]]):
    __returning__ = Items[EducationalInstitution]
    __endpoint__ = "/suggests/educational_institutions"

    text: str
