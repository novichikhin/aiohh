from aiohh.methods.base import BaseMethod
from aiohh.types.dictionaries import District


class GetDistricts(BaseMethod[list[District]]):
    __returning__ = list[District]
    __endpoint__ = "/districts"
