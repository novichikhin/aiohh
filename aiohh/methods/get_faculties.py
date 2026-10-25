from aiohh.methods.base import BaseMethod
from aiohh.types.common import IdName


class GetFaculties(BaseMethod[list[IdName]]):
    __returning__ = list[IdName]
    __endpoint__ = "/educational_institutions/{educational_institution_id}/faculties"

    educational_institution_id: int | str
