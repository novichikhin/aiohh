from aiohh.methods.base import BaseMethod
from aiohh.types.metro import MetroCity


class GetMetro(BaseMethod[list[MetroCity]]):
    __returning__ = list[MetroCity]
    __endpoint__ = "/metro"
