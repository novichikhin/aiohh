from aiohh.methods.base import BaseMethod
from aiohh.types.employer_vacancy import VacancyFieldCondition


class GetVacancyConditions(BaseMethod[dict[str, VacancyFieldCondition | None]]):
    __returning__ = dict[str, VacancyFieldCondition | None]
    __endpoint__ = "/vacancy_conditions"
