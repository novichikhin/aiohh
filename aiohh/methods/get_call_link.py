from aiohh.methods.base import BaseMethod
from aiohh.types.call import CallLink


class GetCallLink(BaseMethod[CallLink]):
    __returning__ = CallLink
    __endpoint__ = "/calls/link"

    resume_id: str
    vacancy_id: int | str | None = None
