from aiohh.methods.base import BaseMethod
from aiohh.types.draft import VacancyDraft


class GetVacancyDraft(BaseMethod[VacancyDraft]):
    __returning__ = VacancyDraft
    __endpoint__ = "/vacancies/drafts/{draft_id}"

    draft_id: int | str
