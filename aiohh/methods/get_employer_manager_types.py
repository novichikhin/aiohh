from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.manager import ManagerType


class GetEmployerManagerTypes(BaseMethod[Items[ManagerType]]):
    __returning__ = Items[ManagerType]
    __endpoint__ = "/employers/{employer_id}/manager_types"

    employer_id: int | str
