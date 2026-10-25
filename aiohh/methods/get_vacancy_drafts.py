from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.draft import VacancyDraftItem


class GetVacancyDrafts(BaseMethod[Page[VacancyDraftItem]]):
    __returning__ = Page[VacancyDraftItem]
    __endpoint__ = "/vacancies/drafts"

    page: int | None = None
    per_page: int | None = None
