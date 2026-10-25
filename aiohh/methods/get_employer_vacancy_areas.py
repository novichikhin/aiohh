from aiohh.methods.base import BaseMethod
from aiohh.types.common import AreaLink, Page


class GetEmployerVacancyAreas(BaseMethod[Page[AreaLink]]):
    __returning__ = Page[AreaLink]
    __endpoint__ = "/employers/{employer_id}/vacancy_areas/active"

    employer_id: int | str
