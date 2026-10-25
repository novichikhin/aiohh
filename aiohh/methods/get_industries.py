from aiohh.methods.base import BaseMethod
from aiohh.types.dictionaries import Industry


class GetIndustries(BaseMethod[list[Industry]]):
    __returning__ = list[Industry]
    __endpoint__ = "/industries"
