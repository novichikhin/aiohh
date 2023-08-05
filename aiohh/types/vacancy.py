from typing import List, Optional

from pydantic import BaseModel, Field

from aiohh.types.base import BaseType


class Area(BaseModel):
    id: str
    name: str
    url: str


class BillingType(BaseModel):
    id: str
    name: Optional[str] = None


class Phone(BaseModel):
    city: str
    country: str
    formatted: str
    number: str
    comment: Optional[str] = None


class Contacts(BaseModel):
    call_tracking_enabled: Optional[bool] = None
    email: Optional[str] = None
    name: Optional[str] = None
    phones: Optional[List[Phone]] = None


class Department(BaseModel):
    id: str
    name: str


class LogoUrls(BaseModel):
    px_90: str = Field(alias="90")
    px_240: str = Field(alias="240")
    original: str


class TargetEmployer(BaseModel):
    count: int


class ApplicantServices(BaseModel):
    target_employer: TargetEmployer


class Employer(BaseModel):
    accredited_it_employer: bool
    name: str
    trusted: bool
    blacklisted: Optional[bool] = None
    applicant_services: Optional[ApplicantServices] = None
    url: Optional[str] = None
    vacancies_url: Optional[str] = None
    alternate_url: Optional[str] = None
    id: Optional[str] = None
    logo_urls: Optional[LogoUrls] = None


class Employment(BaseModel):
    name: str
    id: Optional[str] = None


class Experience(BaseModel):
    id: str
    name: str


class InsiderInterview(BaseModel):
    id: str
    url: str


class KeySkill(BaseModel):
    name: str


class LanguageLevel(BaseModel):
    id: str
    name: str


class Language(BaseModel):
    id: str
    level: LanguageLevel
    name: str


class ProfessionalRole(BaseModel):
    id: str
    name: str


class Salary(BaseModel):
    currency: Optional[str] = None
    lower: Optional[int] = Field(default=None, alias="from")
    gross: Optional[bool] = None
    upper: Optional[int] = Field(default=None, alias="to")


class Schedule(BaseModel):
    id: Optional[str] = None
    name: str


class Test(BaseModel):
    id: Optional[str] = None
    required: Optional[bool] = None


class Type(BaseModel):
    id: str
    name: str


class VacancyPicture(BaseModel):
    blurred_path: Optional[str]
    height: int
    path: str
    width: int


class VacancyConstructorTemplate(BaseModel):
    bottom_picture: Optional[VacancyPicture] = None
    id: int
    name: str
    top_picture: Optional[VacancyPicture] = None


class VideoVacancy(BaseModel):
    video_url: str


class WorkingDay(BaseModel):
    id: str
    name: str


class WorkingTimeInterval(BaseModel):
    id: str
    name: str


class WorkingTimeMode(BaseModel):
    id: str
    name: str


class MetroStation(BaseModel):
    lat: Optional[float] = None
    line_id: str
    line_name: str
    lng: Optional[float] = None
    station_id: str
    station_name: str


class Address(BaseModel):
    building: Optional[str] = None
    city: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    street: Optional[str] = None
    description: Optional[str] = None
    metro_stations: List[MetroStation]


class Vacancy(BaseType):
    accept_handicapped: bool
    accept_incomplete_resumes: bool
    accept_kids: bool
    accept_temporary: Optional[bool] = None
    allow_messages: bool
    alternate_url: str
    apply_alternate_url: str
    archived: bool
    area: Area
    billing_type: Optional[BillingType] = None
    branded_description: Optional[str] = None
    code: Optional[str] = None
    contacts: Optional[Contacts] = None
    created_at: str
    department: Optional[Department] = None
    description: str
    driver_license_types: List[str]
    employer: Optional[Employer] = None
    employment: Optional[Employment] = None
    experience: Optional[Experience] = None
    has_test: bool
    id: str
    initial_created_at: str
    insider_interview: Optional[InsiderInterview] = None
    key_skills: List[KeySkill]
    languages: Optional[List[Language]] = None
    name: str
    negotiations_url: Optional[str] = None
    premium: bool
    professional_roles: List[ProfessionalRole]
    published_at: str
    relations: Optional[List[str]] = None
    response_letter_required: bool
    response_url: Optional[str] = None
    salary: Optional[Salary] = None
    schedule: Optional[Schedule] = None
    suitable_resumes_url: Optional[str] = None
    test: Optional[Test] = None
    type: Optional[Type] = None
    vacancy_constructor_template: Optional[VacancyConstructorTemplate] = None
    video_vacancy: Optional[VideoVacancy] = None
    working_days: Optional[List[WorkingDay]] = None
    working_time_intervals: Optional[List[WorkingTimeInterval]] = None
    working_time_modes: Optional[List[WorkingTimeMode]] = None
    address: Optional[Address] = None
