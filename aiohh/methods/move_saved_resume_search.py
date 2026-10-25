from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class MoveSavedResumeSearch(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/saved_searches/resumes/{saved_search_id}/managers/{manager_id}"

    saved_search_id: int | str
    manager_id: int | str
