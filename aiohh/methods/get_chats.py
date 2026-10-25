from typing import Literal

from pydantic import field_serializer

from aiohh.methods.base import BaseMethod
from aiohh.types.chat import Chat
from aiohh.types.common import Page


class GetChats(BaseMethod[Page[Chat]]):
    __returning__ = Page[Chat]
    __endpoint__ = "/common/chats"

    filter_unread: bool | None = None
    filter_has_text_message: bool | None = None
    vacancy_status: Literal["all", "with", "without"] | None = None
    filter_with_vacancy_ids: list[int | str] | None = None
    page: int | None = None
    per_page: int | None = None

    @field_serializer("filter_with_vacancy_ids")
    def serialize_vacancy_ids(self, value: list[int | str] | None) -> str | None:
        if value is None:
            return None

        return "[" + ",".join(str(item) for item in value) + "]"
