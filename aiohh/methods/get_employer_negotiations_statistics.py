from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import EmployerNegotiationsStatistics


class GetEmployerNegotiationsStatistics(BaseMethod[EmployerNegotiationsStatistics]):
    __returning__ = EmployerNegotiationsStatistics
    __endpoint__ = "/employers/{employer_id}/negotiations_statistics"

    employer_id: int | str
