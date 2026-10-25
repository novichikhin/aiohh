from typing import Literal

from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.token import UserToken


class GetUserToken(BaseMethod[UserToken]):
    __returning__ = UserToken
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/token"
    __body_format__ = BodyFormat.FORM
    __authorized__ = False

    grant_type: Literal["authorization_code"] = "authorization_code"
    client_id: str
    client_secret: str
    code: str
    redirect_uri: str | None = None
    code_verifier: str | None = None
