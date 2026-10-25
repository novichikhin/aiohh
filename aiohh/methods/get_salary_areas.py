from aiohh.methods.base import BaseMethod
from aiohh.types.statistics import SalaryArea


class GetSalaryAreas(BaseMethod[list[SalaryArea]]):
    __returning__ = list[SalaryArea]
    __endpoint__ = "/salary_statistics/dictionaries/salary_areas"
