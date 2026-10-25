from aiohh.methods.base import BaseMethod
from aiohh.types.employer_vacancy import VacancyUpgrades


class GetVacancyUpgrades(BaseMethod[VacancyUpgrades]):
    __returning__ = VacancyUpgrades
    __endpoint__ = "/vacancies/{vacancy_id}/upgrades"

    vacancy_id: int | str
