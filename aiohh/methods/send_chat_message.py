from typing import Any
from uuid import uuid4

from pydantic import model_validator

from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.common import Id


class SendChatMessage(BaseMethod[Id]):
    __returning__ = Id
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/common/chats/{chat_id}/messages"

    chat_id: int | str
    text: str | None = None
    file_upload_ids: list[str] | None = None
    is_automated: bool | None = None
    idempotency_key: str | None = None

    @model_validator(mode="before")
    @classmethod
    def generate_idempotency_key(cls, data: Any) -> Any:
        if isinstance(data, dict) and data.get("idempotency_key") is None:
            return {**data, "idempotency_key": str(uuid4())}

        return data
