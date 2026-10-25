from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.employer import MethodAccess


class GetMethodAccess(BaseMethod[Items[MethodAccess]]):
    __returning__ = Items[MethodAccess]
    __endpoint__ = "/employers/{employer_id}/managers/{manager_id}/method_access"

    employer_id: int | str
    manager_id: int | str
