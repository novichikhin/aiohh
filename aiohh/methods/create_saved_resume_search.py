from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base_resumes_search import BaseResumesSearch


class CreateSavedResumeSearch(BaseResumesSearch[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/saved_searches/resumes"
    __query__ = frozenset(BaseResumesSearch.model_fields) | {
        "employment_form",
        "work_format",
    }

    employment_form: list[str] | None = None
    work_format: list[str] | None = None
