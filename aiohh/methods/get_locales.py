from aiohh.methods.base import BaseMethod
from aiohh.types.dictionaries import Locale


class GetLocales(BaseMethod[list[Locale]]):
    __returning__ = list[Locale]
    __endpoint__ = "/locales"
