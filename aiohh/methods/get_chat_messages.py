from typing import Literal

from aiohh.methods.base import BaseMethod
from aiohh.types.chat import ChatMessages


class GetChatMessages(BaseMethod[ChatMessages]):
    __returning__ = ChatMessages
    __endpoint__ = "/common/chats/{chat_id}/messages"

    chat_id: int | str
    start_message_id: int | str | None = None
    limit: int | None = None
    order: Literal["prev", "next"] | None = None
