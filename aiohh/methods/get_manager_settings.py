from aiohh.methods.base import BaseMethod
from aiohh.types.manager import ManagerSettings


class GetManagerSettings(BaseMethod[ManagerSettings]):
    __returning__ = ManagerSettings
    __endpoint__ = "/employers/{employer_id}/managers/{manager_id}/settings"

    employer_id: int | str
    manager_id: int | str
