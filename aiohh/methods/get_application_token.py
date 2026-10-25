from typing import Literal

from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.token import ApplicationToken


class GetApplicationToken(BaseMethod[ApplicationToken]):
    __returning__ = ApplicationToken
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/token"
    __body_format__ = BodyFormat.FORM
    __authorized__ = False

    grant_type: Literal["client_credentials"] = "client_credentials"
    client_id: str
    client_secret: str
