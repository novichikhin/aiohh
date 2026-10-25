from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class ProlongateVacancy(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/vacancies/{vacancy_id}/prolongate"

    vacancy_id: int | str
