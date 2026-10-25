from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.draft import PublishedDraft


class PublishVacancyDraft(BaseMethod[PublishedDraft]):
    __returning__ = PublishedDraft
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/vacancies/drafts/{draft_id}/publish"

    draft_id: int | str
