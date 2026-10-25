from aiohh.methods.base_vacancies_search import BaseVacanciesSearch


class GetRelatedVacancies(BaseVacanciesSearch):
    __endpoint__ = "/vacancies/{vacancy_id}/related_vacancies"

    vacancy_id: int | str
    excluded_employer_id: list[int | str] | None = None
