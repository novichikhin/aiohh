from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.negotiation import NegotiationMessage


class GetNegotiationMessages(BaseMethod[Page[NegotiationMessage]]):
    __returning__ = Page[NegotiationMessage]
    __endpoint__ = "/negotiations/{negotiation_id}/messages"

    negotiation_id: int | str
    with_text_only: bool | None = None
    page: int | None = None
    per_page: int | None = None
