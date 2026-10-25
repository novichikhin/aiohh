from aiohh.methods.base import BaseMethod
from aiohh.types.chat import ChatParticipant
from aiohh.types.common import Items


class GetChatParticipants(BaseMethod[Items[ChatParticipant]]):
    __returning__ = Items[ChatParticipant]
    __endpoint__ = "/common/chats/{chat_id}/participants"

    chat_id: int | str
