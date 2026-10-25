from aiohh.methods.base import BaseMethod
from aiohh.types.resume import VisitorsPage


class GetVacancyVisitors(BaseMethod[VisitorsPage]):
    __returning__ = VisitorsPage
    __endpoint__ = "/vacancies/{vacancy_id}/visitors"

    vacancy_id: int | str
    page: int | None = None
    per_page: int | None = None
