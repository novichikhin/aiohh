from typing import Generic

from aiohh.methods.base import BaseMethod, ReturningType
from aiohh.types.common import Id
from aiohh.types.vacancy import AutoResponse, Contacts, KeySkill, VacancyTest
from aiohh.types.vacancy_input import (
    SalaryRangeInput,
    VacancyAddressInput,
    VacancyLanguageInput,
)


class BaseVacancyWrite(BaseMethod[ReturningType], Generic[ReturningType]):
    code: str | None = None
    custom_employer_name: str | None = None
    department: Id | None = None
    address: VacancyAddressInput | None = None
    contacts: Contacts | None = None
    show_contacts: bool | None = None
    salary_range: SalaryRangeInput | None = None
    experience: Id | None = None
    employment_form: Id | None = None
    work_format: list[Id] | None = None
    work_schedule_by_days: list[Id] | None = None
    working_hours: list[Id] | None = None
    fly_in_fly_out_duration: list[Id] | None = None
    civil_law_contracts: list[Id] | None = None
    professional_roles: list[Id] | None = None
    key_skills: list[KeySkill] | None = None
    languages: list[VacancyLanguageInput] | None = None
    driver_license_types: list[Id] | None = None
    age_restriction: Id | None = None
    branded_template: Id | None = None
    test: VacancyTest | None = None
    auto_response: AutoResponse | None = None
    allow_messages: bool | None = None
    response_url: str | None = None
    response_letter_required: bool | None = None
    response_notifications: bool | None = None
    accept_incomplete_resumes: bool | None = None
    accept_labor_contract: bool | None = None
    internship: bool | None = None
    night_shifts: bool | None = None
    inclusiveness_description: str | None = None
    inclusiveness_types: list[str] | None = None
