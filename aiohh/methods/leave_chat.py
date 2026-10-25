from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class LeaveChat(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/common/chats/{chat_id}/leave"

    chat_id: int | str
