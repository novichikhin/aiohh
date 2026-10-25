from aiohh.methods.base import BaseMethod
from aiohh.types.common import IdName, Items


class GetEmployerDepartments(BaseMethod[Items[IdName]]):
    __returning__ = Items[IdName]
    __endpoint__ = "/employers/{employer_id}/departments"

    employer_id: int | str
