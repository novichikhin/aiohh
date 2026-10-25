from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.common import Id
from aiohh.types.manager import ManagerPhone


class AddEmployerManager(BaseMethod[Id]):
    __returning__ = Id
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/employers/{employer_id}/managers"

    employer_id: int | str
    email: str
    first_name: str
    last_name: str
    middle_name: str | None = None
    position: str
    area: Id
    phone: ManagerPhone
    additional_phone: ManagerPhone | None = None
    is_main_contact_person: bool
    manager_type: Id = Id(id="manager")
    permissions: list[Id] | None = None
