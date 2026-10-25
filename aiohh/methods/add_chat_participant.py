from pydantic import Field

from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class AddChatParticipant(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/common/chats/{chat_id}/participants"

    chat_id: int | str
    manager_id: int | str = Field(alias="id")
