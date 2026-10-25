from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import ManagerNegotiationsStatistics


class GetManagerNegotiationsStatistics(BaseMethod[ManagerNegotiationsStatistics]):
    __returning__ = ManagerNegotiationsStatistics
    __endpoint__ = (
        "/employers/{employer_id}/managers/{manager_id}/negotiations_statistics"
    )

    employer_id: int | str
    manager_id: int | str
