from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base_vacancy_write import BaseVacancyWrite
from aiohh.types.common import Id
from aiohh.types.vacancy_input import VacancyPropertiesInput


class PublishVacancy(BaseVacancyWrite[Id]):
    __returning__ = Id
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/vacancies"
    __query__ = frozenset({"ignore_duplicates"})

    name: str
    description: str
    area: Id
    vacancy_properties: VacancyPropertiesInput
    manager: Id | None = None
    employer_service_id: str | None = None
    previous_id: str | None = None
    closed_for_applicants: bool | None = None
    ignore_duplicates: bool | None = None
