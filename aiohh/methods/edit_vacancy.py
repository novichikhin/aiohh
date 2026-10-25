from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base_vacancy_write import BaseVacancyWrite
from aiohh.types.common import Id
from aiohh.types.vacancy_input import VacancyPropertiesInput


class EditVacancy(BaseVacancyWrite[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/vacancies/{vacancy_id}"
    __query__ = frozenset({"ignore_duplicates", "ignore_replacement_warning"})

    vacancy_id: int | str
    name: str | None = None
    description: str | None = None
    vacancy_properties: VacancyPropertiesInput | None = None
    manager: Id | None = None
    ignore_duplicates: bool | None = None
    ignore_replacement_warning: bool | None = None
