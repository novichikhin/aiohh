from aiohh.methods.base import BaseMethod
from aiohh.types.statistics import SalaryProfessionalArea


class GetSalaryProfessionalAreas(BaseMethod[list[SalaryProfessionalArea]]):
    __returning__ = list[SalaryProfessionalArea]
    __endpoint__ = "/salary_statistics/dictionaries/professional_areas"
