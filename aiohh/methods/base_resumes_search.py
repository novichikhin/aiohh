from datetime import date, datetime
from typing import Generic

from aiohh.methods.base import BaseMethod, ReturningType
from aiohh.types.resume import ResumeSearchText


class BaseResumesSearch(BaseMethod[ReturningType], Generic[ReturningType]):
    text: list[ResumeSearchText] | None = None
    area: list[int | str] | None = None
    metro: list[int | str] | None = None
    relocation: str | None = None
    period: int | None = None
    date_from: date | datetime | None = None
    date_to: date | datetime | None = None
    age_from: int | None = None
    age_to: int | None = None
    gender: str | None = None
    experience: list[str] | None = None
    skill: list[int | str] | None = None
    language: list[str] | None = None
    label: list[str] | None = None
    currency: str | None = None
    salary_from: int | None = None
    salary_to: int | None = None
    professional_role: list[int | str] | None = None
    citizenship: list[int | str] | None = None
    work_ticket: list[int | str] | None = None
    educational_institution: list[int | str] | None = None
    driver_license_types: list[str] | None = None
    search_in_responses: bool | None = None
    by_text_prefix: bool | None = None
    order_by: str | None = None
    page: int | None = None
    per_page: int | None = None
