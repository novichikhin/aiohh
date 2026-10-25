from datetime import date, datetime
from typing import Any

from pydantic import Field

from aiohh.types.base import BaseType
from aiohh.types.common import AreaLink, Id, IdName, Link, Page
from aiohh.types.employer import EmployerShort
from aiohh.types.me import JobSearchStatus
from aiohh.types.metro import MetroLineInfo


class AreaReference(BaseType):
    id: str
    name: str | None = None
    url: str | None = None


class ResumeDownload(BaseType):
    pdf: Link
    rtf: Link


class ResumeActions(BaseType):
    download: ResumeDownload | None = None
    download_with_contact: ResumeDownload | None = None
    get_with_contact: Link | None = None


class ResumePhoto(BaseType):
    small: str | None = None
    medium: str | None = None
    large: str | None = None


class ResumeSalary(BaseType):
    amount: int | None = None
    currency: str | None = None


class ResumeTotalExperience(BaseType):
    months: int | None = None


class ResumeCertificate(BaseType):
    title: str | None = None
    type: str | None = None
    achieved_at: str | None = None
    owner: str | None = None
    url: str | None = None


class EducationPrimary(BaseType):
    id: str | None = None
    name: str
    name_id: str | None = None
    organization: str | None = None
    organization_id: str | None = None
    result: str | None = None
    result_id: str | None = None
    university_acronym: str | None = None
    education_level: IdName | None = None
    year: int


class EducationAdditional(BaseType):
    id: str | None = None
    name: str
    organization: str | None = None
    result: str | None = None
    year: int


class EducationElementary(BaseType):
    id: str | None = None
    name: str
    year: int


class ResumeEducation(BaseType):
    level: IdName | None = None
    primary: list[EducationPrimary] | None = None
    additional: list[EducationAdditional] | None = None
    attestation: list[EducationAdditional] | None = None
    elementary: list[EducationElementary] | None = None


class ExperienceVerification(BaseType):
    can_modify: bool | None = None
    status: str | None = None


class ResumeExperience(BaseType):
    id: str | None = None
    position: str | None = None
    start: date | None = None
    end: date | None = None
    company: str | None = None
    company_id: str | None = None
    company_url: str | None = None
    area: AreaLink | None = None
    employer: EmployerShort | None = None
    industries: list[IdName] = []
    description: str | None = None
    verification: ExperienceVerification | None = None


class ExperienceGroup(BaseType):
    duration: int
    experience_ids: list[str] = []


class ResumeOwnerCommentsCounters(BaseType):
    total: int


class ResumeOwnerComments(BaseType):
    url: str
    counters: ResumeOwnerCommentsCounters


class ResumeOwner(BaseType):
    id: str
    comments: ResumeOwnerComments | None = None


class ResumeLastNegotiation(BaseType):
    created_at: datetime
    employer_state: IdName


class NegotiationsHistoryItem(ResumeLastNegotiation):
    with_message: bool


class NegotiationsHistoryVacancy(BaseType):
    id: str
    name: str
    url: str
    archived: bool
    can_edit: bool
    messages_url: str
    negotiations_url: str
    items: list[NegotiationsHistoryItem] = []


class NegotiationsHistory(BaseType):
    vacancies: list[NegotiationsHistoryVacancy] = []


class ResumeNegotiationsHistory(BaseType):
    url: str
    vacancies: list[NegotiationsHistoryVacancy] | None = None


class BaseResume(BaseType):
    id: str
    title: str | None = None
    url: str | None = None
    alternate_url: str
    real_id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    age: int | None = None
    gender: IdName | None = None
    area: AreaLink | None = None
    photo: ResumePhoto | None = None
    salary: ResumeSalary | None = None
    total_experience: ResumeTotalExperience | None = None
    experience: list[ResumeExperience] = []
    experience_group_by_company: list[ExperienceGroup] | None = None
    education: ResumeEducation | None = None
    certificate: list[ResumeCertificate] = []
    citizenship: list[AreaReference] = []
    work_ticket: list[AreaReference] = []
    employment_form: list[IdName] = []
    work_format: list[IdName] = []
    hidden_fields: list[IdName] = []
    platform: Id | None = None
    actions: ResumeActions | None = None
    download: ResumeDownload | None = None
    download_as_employer: ResumeDownload | None = None
    can_view_full_info: bool | None = None
    contact_view_status: str | None = None
    contacts_open_until_date: datetime | None = None
    marked: bool | None = None
    favorited: bool | None = None
    viewed: bool | None = None
    owner: ResumeOwner | None = None
    tags: list[Id] = []
    job_search_status: JobSearchStatus | None = None
    negotiations_history: ResumeNegotiationsHistory | None = None


class ResumeItem(BaseResume):
    last_negotiation: ResumeLastNegotiation | None = None


class ResumesPage(Page[ResumeItem]):
    pass


class VisitorsPage(Page[ResumeItem]):
    hidden_on_page: int | None = None


class ContactPhone(BaseType):
    country: str
    city: str
    number: str
    formatted: str


class ContactLinks(BaseType):
    web: str | None = None
    android: str | None = None
    ios: str | None = None


class ResumeContact(BaseType):
    type: IdName
    value: ContactPhone | str | None = None
    preferred: bool
    comment: str | None = None
    contact_value: str | None = None
    need_verification: bool | None = None
    verified: bool | None = None
    links: ContactLinks | None = None


class ResumeLanguage(IdName):
    level: IdName | None = None


class ResumeMetroStation(BaseType):
    id: str
    name: str | None = None
    lat: float | None = None
    lng: float | None = None
    order: int | None = None
    line: MetroLineInfo


class ResumePaidService(BaseType):
    id: str
    name: str
    description: str | None = None
    active: bool | None = None
    expires: datetime | None = None


class ResumeRecommendation(BaseType):
    name: str
    position: str
    organization: str
    contact: str | None = None


class ResumeRelocation(BaseType):
    type: IdName
    area: list[AreaLink] = []
    district: list[IdName] = []


class ResumeSite(BaseType):
    type: IdName | None = None
    url: str | None = None


class ResumeComplaintStatus(BaseType):
    applicant_topics_are_hidden: bool | None = None


class ResumePortfolio(BaseType):
    small: str
    medium: str
    large: str | None = None
    description: str | None = None


class Resume(BaseResume):
    birth_date: date | None = None
    contact: list[ResumeContact] = []
    skills: str | None = None
    skill_set: list[str] = []
    language: list[ResumeLanguage] = []
    professional_roles: list[IdName] | None = None
    employments: list[IdName] = []
    schedules: list[IdName] = []
    business_trip_readiness: IdName | None = None
    travel_time: IdName | None = None
    relocation: ResumeRelocation | None = None
    resume_locale: IdName | None = None
    metro: ResumeMetroStation | None = None
    driver_license_types: list[Id] = []
    has_vehicle: bool | None = None
    has_medical_book: bool | None = None
    has_self_employment: bool | None = None
    recommendation: list[ResumeRecommendation] = []
    site: list[ResumeSite] = []
    portfolio: list[ResumePortfolio] = []
    paid_services: list[ResumePaidService] = []
    complaint_status: ResumeComplaintStatus | None = None
    view_without_contacts_reason: str | None = None
    creds: dict[str, Any] | None = None


class CountLink(Link):
    count: int


class SavedResumeSearch(BaseType):
    id: str
    name: str
    created_at: datetime
    subscription: bool
    items: CountLink
    new_items: CountLink


class ResumeSearchText(BaseType):
    text: str
    logic: str | None = Field(default=None, alias="text.logic")
    field: str | None = Field(default=None, alias="text.field")
    period: str | None = Field(default=None, alias="text.period")
    company_size: str | None = Field(default=None, alias="text.company_size")
