from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import Negotiation


class GetNegotiation(BaseMethod[Negotiation]):
    __returning__ = Negotiation
    __endpoint__ = "/negotiations/{negotiation_id}"

    negotiation_id: int | str
