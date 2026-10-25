from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class DeleteChatMessage(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.DELETE
    __endpoint__ = "/common/chats/{chat_id}/messages/{message_id}"

    chat_id: int | str
    message_id: int | str
