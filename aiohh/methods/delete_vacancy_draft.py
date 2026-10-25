from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class DeleteVacancyDraft(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.DELETE
    __endpoint__ = "/vacancies/drafts/{draft_id}"

    draft_id: int | str
