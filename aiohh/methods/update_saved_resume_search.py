from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class UpdateSavedResumeSearch(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/saved_searches/resumes/{saved_search_id}"
    __query__ = frozenset({"name", "subscription"})

    saved_search_id: int | str
    name: str | None = None
    subscription: bool | None = None
