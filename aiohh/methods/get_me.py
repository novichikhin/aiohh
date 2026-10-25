from aiohh.methods.base import BaseMethod
from aiohh.types.me import Me


class GetMe(BaseMethod[Me]):
    __returning__ = Me
    __endpoint__ = "/me"
