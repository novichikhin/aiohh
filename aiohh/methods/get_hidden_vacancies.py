from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.employer_vacancy import EmployerVacancy


class GetHiddenVacancies(BaseMethod[Page[EmployerVacancy]]):
    __returning__ = Page[EmployerVacancy]
    __endpoint__ = "/employers/{employer_id}/vacancies/hidden"

    employer_id: int | str
    manager_id: list[int | str] | None = None
    order_by: str | None = None
    page: int | None = None
    per_page: int | None = None
