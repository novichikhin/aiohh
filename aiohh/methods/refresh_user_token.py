from typing import Literal

from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.token import UserToken


class RefreshUserToken(BaseMethod[UserToken]):
    __returning__ = UserToken
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/token"
    __body_format__ = BodyFormat.FORM
    __authorized__ = False

    grant_type: Literal["refresh_token"] = "refresh_token"
    refresh_token: str
