from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class MarkChatMessageRead(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/common/chats/{chat_id}/message/{message_id}/read"

    chat_id: int | str
    message_id: int | str
