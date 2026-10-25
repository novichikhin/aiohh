from aiohh.methods.base import BaseMethod
from aiohh.types.resume import SavedResumeSearch


class GetSavedResumeSearch(BaseMethod[SavedResumeSearch]):
    __returning__ = SavedResumeSearch
    __endpoint__ = "/saved_searches/resumes/{saved_search_id}"

    saved_search_id: int | str
