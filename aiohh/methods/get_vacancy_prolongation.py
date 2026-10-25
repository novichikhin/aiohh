from aiohh.methods.base import BaseMethod
from aiohh.types.employer_vacancy import VacancyProlongation


class GetVacancyProlongation(BaseMethod[VacancyProlongation]):
    __returning__ = VacancyProlongation
    __endpoint__ = "/vacancies/{vacancy_id}/prolongate"

    vacancy_id: int | str
