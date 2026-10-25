from aiohh.types.base import BaseType


class ApplicationToken(BaseType):
    access_token: str
    token_type: str


class UserToken(ApplicationToken):
    refresh_token: str
    expires_in: int
