from aiohh.methods.base_vacancies_search import BaseVacanciesSearch


class SearchVacancies(BaseVacanciesSearch):
    __endpoint__ = "/vacancies"

    accept_temporary: bool | None = None
    excluded_text: str | None = None
