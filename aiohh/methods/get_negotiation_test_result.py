from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import NegotiationTestResult


class GetNegotiationTestResult(BaseMethod[NegotiationTestResult]):
    __returning__ = NegotiationTestResult
    __endpoint__ = "/negotiations/{negotiation_id}/test/solution"

    negotiation_id: int | str
