from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.chat import ChatFileUploadLink


class GetChatFileUploadLink(BaseMethod[ChatFileUploadLink]):
    __returning__ = ChatFileUploadLink
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/common/chats/files/upload_links"
