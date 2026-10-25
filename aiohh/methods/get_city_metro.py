from aiohh.methods.base import BaseMethod
from aiohh.types.metro import MetroCity


class GetCityMetro(BaseMethod[MetroCity]):
    __returning__ = MetroCity
    __endpoint__ = "/metro/{city_id}"

    city_id: int | str
