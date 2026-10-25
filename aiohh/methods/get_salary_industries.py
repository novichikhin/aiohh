from aiohh.methods.base import BaseMethod
from aiohh.types.dictionaries import Industry


class GetSalaryIndustries(BaseMethod[list[Industry]]):
    __returning__ = list[Industry]
    __endpoint__ = "/salary_statistics/dictionaries/salary_industries"
