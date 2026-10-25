from aiohh.methods.base import BaseMethod
from aiohh.types.chat import UnreadChatsCount


class GetUnreadChatsCount(BaseMethod[UnreadChatsCount]):
    __returning__ = UnreadChatsCount
    __endpoint__ = "/common/chats/counters/unread"
