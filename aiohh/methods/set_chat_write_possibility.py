from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class SetChatWritePossibility(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/common/chats/{chat_id}/write_possibility"
    __query__ = frozenset({"applicant_write_possibility"})

    chat_id: int | str
    applicant_write_possibility: bool
