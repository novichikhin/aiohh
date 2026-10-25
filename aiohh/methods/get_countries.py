from aiohh.methods.base import BaseMethod
from aiohh.types.common import AreaLink


class GetCountries(BaseMethod[list[AreaLink]]):
    __returning__ = list[AreaLink]
    __endpoint__ = "/areas/countries"
