from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.employer_vacancy import VacancyStatsItem


class GetVacancyStats(BaseMethod[Items[VacancyStatsItem]]):
    __returning__ = Items[VacancyStatsItem]
    __endpoint__ = "/vacancies/{vacancy_id}/stats"

    vacancy_id: int | str
