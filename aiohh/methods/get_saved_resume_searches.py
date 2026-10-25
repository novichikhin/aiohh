from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.resume import SavedResumeSearch


class GetSavedResumeSearches(BaseMethod[Page[SavedResumeSearch]]):
    __returning__ = Page[SavedResumeSearch]
    __endpoint__ = "/saved_searches/resumes"

    page: int | None = None
    per_page: int | None = None
