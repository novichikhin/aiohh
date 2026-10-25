from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class DeleteSavedResumeSearch(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.DELETE
    __endpoint__ = "/saved_searches/resumes/{saved_search_id}"

    saved_search_id: int | str
