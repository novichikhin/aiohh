from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.employer import EmployerService


class GetEmployerServices(BaseMethod[Items[EmployerService]]):
    __returning__ = Items[EmployerService]
    __endpoint__ = "/employers/{employer_id}/services/payable_api_actions/active"

    employer_id: int | str
