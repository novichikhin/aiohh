from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class DisableDraftAutoPublication(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.DELETE
    __endpoint__ = "/vacancies/auto_publication"

    draft_id: int | str
