from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.common import Id
from aiohh.types.manager import ManagerPhone


class EditEmployerManager(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/employers/{employer_id}/managers/{manager_id}"

    employer_id: int | str
    manager_id: int | str
    position: str | None = None
    phone: ManagerPhone | None = None
    additional_phone: ManagerPhone | None = None
    permissions: list[Id] | None = None
