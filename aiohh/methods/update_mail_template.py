from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class UpdateMailTemplate(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/employers/{employer_id}/mail_templates/{template_id}"

    employer_id: int | str
    template_id: int | str
    text: str
