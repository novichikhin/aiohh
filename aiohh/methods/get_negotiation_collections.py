from typing import Literal

from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import NegotiationsCollections


class GetNegotiationCollections(BaseMethod[NegotiationsCollections]):
    __returning__ = NegotiationsCollections
    __endpoint__ = "/negotiations"

    vacancy_id: int | str | None = None
    status: str | None = None
    has_updates: bool | None = None
    with_job_search_status: bool | None = None
    with_generated_collections: bool | None = None
    order_by: str | None = None
    order: Literal["asc", "desc"] | None = None
    page: int | None = None
    per_page: int | None = None
