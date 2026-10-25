from typing import Any

from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class CreateChatWithoutVacancy(BaseMethod[dict[str, Any]]):
    __returning__ = dict[str, Any]
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/common/chats/without_vacancy"

    resume_hash: str
    first_message: str | None = None
