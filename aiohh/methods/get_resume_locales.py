from aiohh.methods.base import BaseMethod
from aiohh.types.dictionaries import Locale


class GetResumeLocales(BaseMethod[list[Locale]]):
    __returning__ = list[Locale]
    __endpoint__ = "/locales/resume"
