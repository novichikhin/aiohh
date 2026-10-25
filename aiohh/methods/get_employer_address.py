from aiohh.methods.base import BaseMethod
from aiohh.types.employer import EmployerAddress


class GetEmployerAddress(BaseMethod[EmployerAddress]):
    __returning__ = EmployerAddress
    __endpoint__ = "/employers/{employer_id}/addresses/{address_id}"

    employer_id: int | str
    address_id: int | str
    with_manager: bool | None = None
