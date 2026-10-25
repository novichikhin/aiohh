from datetime import date, datetime

from aiohh.methods.base import BaseMethod
from aiohh.types.vacancy import VacanciesPage


class BaseVacanciesSearch(BaseMethod[VacanciesPage]):
    __returning__ = VacanciesPage

    text: str | None = None
    search_field: list[str] | None = None
    experience: list[str] | None = None
    employment_form: list[str] | None = None
    work_format: list[str] | None = None
    work_schedule_by_days: list[str] | None = None
    working_hours: list[str] | None = None
    area: list[int | str] | None = None
    metro: list[int | str] | None = None
    professional_role: list[int | str] | None = None
    industry: list[int | str] | None = None
    employer_id: list[int | str] | None = None
    currency: str | None = None
    salary: int | None = None
    salary_frequency: list[str] | None = None
    salary_mode: str | None = None
    label: list[str] | None = None
    education: list[str] | None = None
    driver_license_types: list[str] | None = None
    period: int | None = None
    date_from: date | datetime | None = None
    date_to: date | datetime | None = None
    top_lat: float | None = None
    bottom_lat: float | None = None
    left_lng: float | None = None
    right_lng: float | None = None
    order_by: str | None = None
    sort_point_lat: float | None = None
    sort_point_lng: float | None = None
    clusters: bool | None = None
    describe_arguments: bool | None = None
    no_magic: bool | None = None
    responses_count_enabled: bool | None = None
    page: int | None = None
    per_page: int | None = None
