from datetime import datetime

from aiohh.types.base import BaseType
from aiohh.types.common import Id, IdName


class IdNameUid(IdName):
    uid: str


class Currency(BaseType):
    code: str
    abbr: str
    name: str
    default: bool
    in_use: bool
    rate: float


class EmploymentFormItem(IdName):
    duration: str | None = None


class InclusivenessType(IdName):
    legacy: bool


class Dictionaries(BaseType):
    age_restriction: list[IdName] = []
    applicant_comment_access_type: list[IdName] = []
    applicant_comments_order: list[IdName] = []
    applicant_negotiation_status: list[IdName] = []
    business_trip_readiness: list[IdName] = []
    civil_law_contracts: list[IdName] = []
    currency: list[Currency] = []
    driver_license_types: list[Id] = []
    education_level: list[IdName] = []
    employer_active_vacancies_order: list[IdName] = []
    employer_archived_vacancies_order: list[IdName] = []
    employer_hidden_vacancies_order: list[IdName] = []
    employer_relation: list[IdName] = []
    employer_type: list[IdName] = []
    employment: list[IdName] = []
    employment_form: list[EmploymentFormItem] = []
    experience: list[IdName] = []
    fly_in_fly_out_duration: list[IdName] = []
    gender: list[IdName] = []
    inclusiveness_types: list[InclusivenessType] = []
    job_search_statuses_applicant: list[IdName] = []
    job_search_statuses_employer: list[IdName] = []
    language_level: list[IdName] = []
    linked_socials: list[IdName] = []
    messaging_status: list[IdName] = []
    negotiations_order: list[IdName] = []
    negotiations_participant_type: list[IdName] = []
    negotiations_state: list[IdName] = []
    phone_call_status: list[IdName] = []
    preferred_contact_type: list[IdName] = []
    relocation_type: list[IdName] = []
    resume_access_type: list[IdName] = []
    resume_contacts_site_type: list[IdName] = []
    resume_employment_form: list[IdName] = []
    resume_hidden_fields: list[IdName] = []
    resume_moderation_note: list[IdName] = []
    resume_search_experience_period: list[IdName] = []
    resume_search_fields: list[IdName] = []
    resume_search_label: list[IdName] = []
    resume_search_logic: list[IdName] = []
    resume_search_order: list[IdName] = []
    resume_search_relocation: list[IdName] = []
    resume_status: list[IdName] = []
    resume_work_format: list[IdName] = []
    salary_range_frequency: list[IdName] = []
    salary_range_mode: list[IdName] = []
    schedule: list[IdNameUid] = []
    setka_access_type: list[IdName] = []
    travel_time: list[IdName] = []
    vacancy_billing_type: list[IdName] = []
    vacancy_cluster: list[IdName] = []
    vacancy_label: list[IdName] = []
    vacancy_not_prolonged_reason: list[IdName] = []
    vacancy_relation: list[IdName] = []
    vacancy_search_employment_form: list[IdName] = []
    vacancy_search_fields: list[IdName] = []
    vacancy_search_order: list[IdName] = []
    vacancy_type: list[IdName] = []
    work_format: list[IdName] = []
    work_schedule_by_days: list[IdName] = []
    working_days: list[IdName] = []
    working_hours: list[IdName] = []
    working_time_intervals: list[IdName] = []
    working_time_modes: list[IdName] = []


class Industry(IdName):
    industries: list[IdName] = []


class ProfessionalRole(IdName):
    accept_incomplete_resumes: bool
    is_default: bool
    search_deprecated: bool | None = None
    search_deprecated_datetime: datetime | None = None
    select_deprecated: bool | None = None
    select_deprecated_datetime: datetime | None = None


class ProfessionalRoleCategory(BaseType):
    id: str
    name: str | None = None
    roles: list[ProfessionalRole] = []


class ProfessionalRolesCatalog(BaseType):
    categories: list[ProfessionalRoleCategory]


class Language(IdName):
    uid: str


class Locale(IdName):
    current: bool | None = None


class Skill(BaseType):
    id: str
    text: str


class EducationalInstitution(BaseType):
    id: str
    text: str
    acronym: str | None = None
    synonyms: str | None = None
    area: IdName


class District(IdName):
    area_id: str
