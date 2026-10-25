from datetime import datetime

from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base_vacancy_write import BaseVacancyWrite
from aiohh.types.common import Id
from aiohh.types.draft import DraftResponse
from aiohh.types.vacancy_input import VacancyPropertiesInput


class CreateVacancyDraft(BaseVacancyWrite[DraftResponse]):
    __returning__ = DraftResponse
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/vacancies/drafts"

    name: str | None = None
    description: str | None = None
    area: Id | None = None
    areas: list[Id] | None = None
    assigned_manager_id: str | None = None
    employer_service_id: str | None = None
    scheduled_at: datetime | None = None
    closed_for_applicants: bool | None = None
    vacancy_properties: VacancyPropertiesInput | None = None
