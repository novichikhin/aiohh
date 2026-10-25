from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import MailTemplate


class GetMailTemplates(BaseMethod[list[MailTemplate]]):
    __returning__ = list[MailTemplate]
    __endpoint__ = "/employers/{employer_id}/mail_templates"

    employer_id: int | str
