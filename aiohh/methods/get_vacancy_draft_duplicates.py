from aiohh.methods.base import BaseMethod
from aiohh.types.draft import VacancyDuplicates


class GetVacancyDraftDuplicates(BaseMethod[VacancyDuplicates]):
    __returning__ = VacancyDuplicates
    __endpoint__ = "/vacancies/drafts/{draft_id}/duplicates"

    draft_id: int | str
