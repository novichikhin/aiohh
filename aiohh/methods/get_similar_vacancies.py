from aiohh.methods.base_vacancies_search import BaseVacanciesSearch


class GetSimilarVacancies(BaseVacanciesSearch):
    __endpoint__ = "/vacancies/{vacancy_id}/similar_vacancies"

    vacancy_id: int | str
    excluded_employer_id: list[int | str] | None = None
