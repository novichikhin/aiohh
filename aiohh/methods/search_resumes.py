from datetime import datetime

from aiohh.methods.base_resumes_search import BaseResumesSearch
from aiohh.types.resume import ResumesPage


class SearchResumes(BaseResumesSearch[ResumesPage]):
    __returning__ = ResumesPage
    __endpoint__ = "/resumes"

    employment_form: list[str] | None = None
    work_format: list[str] | None = None
    education_levels: list[str] | None = None
    job_search_status: list[str] | None = None
    business_trip_readiness: list[str] | None = None
    district: list[int | str] | None = None
    filter_exp_industry: str | None = None
    filter_exp_period: str | None = None
    vacancy_id: int | str | None = None
    resume: str | None = None
    folder: list[int | str] | None = None
    include_all_folders: bool | None = None
    with_job_search_status: bool | None = None
    saved_search_id: int | str | None = None
    search_by_vacancy_id: int | str | None = None
    last_used: datetime | None = None
    last_used_timestamp: str | None = None
