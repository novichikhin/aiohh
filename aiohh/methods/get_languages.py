from aiohh.methods.base import BaseMethod
from aiohh.types.dictionaries import Language


class GetLanguages(BaseMethod[list[Language]]):
    __returning__ = list[Language]
    __endpoint__ = "/languages"
