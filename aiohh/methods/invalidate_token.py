from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class InvalidateToken(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.DELETE
    __endpoint__ = "/token"
