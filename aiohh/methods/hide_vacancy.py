from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class HideVacancy(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/employers/{employer_id}/vacancies/hidden/{vacancy_id}"

    employer_id: int | str
    vacancy_id: int | str
