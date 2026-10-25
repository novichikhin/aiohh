from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class SetPreferredNegotiationsOrder(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/vacancies/{vacancy_id}/preferred_negotiations_order"
    __body_format__ = BodyFormat.FORM

    vacancy_id: int | str
    order: str
