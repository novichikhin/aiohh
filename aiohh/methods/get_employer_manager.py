from aiohh.methods.base import BaseMethod
from aiohh.types.manager import EmployerManager


class GetEmployerManager(BaseMethod[EmployerManager]):
    __returning__ = EmployerManager
    __endpoint__ = "/employers/{employer_id}/managers/{manager_id}"

    employer_id: int | str
    manager_id: int | str
