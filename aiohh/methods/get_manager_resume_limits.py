from aiohh.methods.base import BaseMethod
from aiohh.types.manager import ManagerResumeLimits


class GetManagerResumeLimits(BaseMethod[ManagerResumeLimits]):
    __returning__ = ManagerResumeLimits
    __endpoint__ = "/employers/{employer_id}/managers/{manager_id}/limits/resume"

    employer_id: int | str
    manager_id: int | str
