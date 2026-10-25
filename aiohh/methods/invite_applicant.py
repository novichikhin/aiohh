from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class InviteApplicant(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/negotiations/phone_interview"
    __body_format__ = BodyFormat.FORM

    vacancy_id: int | str
    resume_id: str
    message: str | None = None
    send_sms: bool | None = None
