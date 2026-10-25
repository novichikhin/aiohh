from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.employer_vacancy import EmployerVacancy


class GetActiveVacancies(BaseMethod[Page[EmployerVacancy]]):
    __returning__ = Page[EmployerVacancy]
    __endpoint__ = "/employers/{employer_id}/vacancies/active"

    employer_id: int | str
    text: str | None = None
    area: int | str | None = None
    manager_ids: list[int | str] | None = None
    department_id: str | None = None
    resume_id: str | None = None
    all_accessible: bool | None = None
    order_by: str | None = None
    page: int | None = None
    per_page: int | None = None
