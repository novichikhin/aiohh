from aiohh.methods.base import BaseMethod
from aiohh.types.chat import ChatFilesConditions


class GetChatFilesConditions(BaseMethod[ChatFilesConditions]):
    __returning__ = ChatFilesConditions
    __endpoint__ = "/common/chats/files/conditions"
