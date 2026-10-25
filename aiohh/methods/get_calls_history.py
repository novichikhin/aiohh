from datetime import datetime
from typing import Literal

from aiohh.methods.base import BaseMethod
from aiohh.types.call import CallsHistory


class GetCallsHistory(BaseMethod[CallsHistory]):
    __returning__ = CallsHistory
    __endpoint__ = "/calls/history"

    vacancy_id: list[int | str] | None = None
    date_from: datetime | None = None
    date_to: datetime | None = None
    direction: Literal["outgoing", "incoming"] | None = None
    successful: bool | None = None
    with_resume: bool | None = None
    without_vacancy: bool | None = None
    link_id: str | None = None
    next_cursor: str | None = None
    previous_cursor: str | None = None
    per_page: int | None = None
