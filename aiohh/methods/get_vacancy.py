from typing import ClassVar

from aiohh.methods.base import BaseMethod
from aiohh.types.vacancy import Vacancy


class GetVacancy(BaseMethod[Vacancy]):
    __returning__ = Vacancy

    url: ClassVar[str] = "https://api.hh.ru/vacancies/{vacancy_id}"
    http_method: ClassVar[str] = "GET"

    vacancy_id: int
    locale: str = "RU"
    host: str = "hh.ru"
