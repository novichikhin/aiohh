from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class MarkNegotiationsRead(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/negotiations/read"
    __body_format__ = BodyFormat.FORM

    topic_id: list[int | str]
