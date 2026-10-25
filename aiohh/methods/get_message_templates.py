from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import MessageTemplates


class GetMessageTemplates(BaseMethod[MessageTemplates]):
    __returning__ = MessageTemplates
    __endpoint__ = "/message_templates/{template}"

    template: str
    topic_id: int | str | None = None
    vacancy_id: int | str | None = None
    resume_id: str | None = None
