from aiohh.methods.base import BaseMethod
from aiohh.types.vacancy import Vacancy


class GetVacancy(BaseMethod[Vacancy]):
    __returning__ = Vacancy
    __endpoint__ = "/vacancies/{vacancy_id}"

    vacancy_id: int | str
