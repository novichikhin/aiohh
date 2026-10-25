from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.dictionaries import EducationalInstitution


class GetEducationalInstitutions(BaseMethod[Items[EducationalInstitution]]):
    __returning__ = Items[EducationalInstitution]
    __endpoint__ = "/educational_institutions"

    id: list[int | str]
