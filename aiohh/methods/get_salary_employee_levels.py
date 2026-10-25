from aiohh.methods.base import BaseMethod
from aiohh.types.statistics import IdNameDescription


class GetSalaryEmployeeLevels(BaseMethod[list[IdNameDescription]]):
    __returning__ = list[IdNameDescription]
    __endpoint__ = "/salary_statistics/dictionaries/employee_levels"
