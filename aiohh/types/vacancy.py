from datetime import datetime

from pydantic import Field

from aiohh.types.base import BaseType
from aiohh.types.common import AreaLink, Id, IdName, LogoUrls, Page


class SalaryRange(BaseType):
    currency: str
    gross: bool
    from_: int | None = Field(default=None, alias="from")
    to: int | None = None
    frequency: IdName | None = None
    mode: IdName | None = None


class Phone(BaseType):
    country: str | None = None
    city: str | None = None
    number: str | None = None
    formatted: str | None = None
    comment: str | None = None


class Contacts(BaseType):
    name: str | None = None
    call_tracking_enabled: bool | None = None
    phones: list[Phone] | None = None


class AddressMetroStation(BaseType):
    station_id: str
    station_name: str
    line_id: str
    line_name: str
    hex_color: str | None = None
    lat: float | None = None
    lng: float | None = None


class Address(BaseType):
    id: str | None = None
    city: str | None = None
    street: str | None = None
    building: str | None = None
    description: str | None = None
    raw: str | None = None
    lat: float | None = None
    lng: float | None = None
    metro: AddressMetroStation | None = None
    metro_stations: list[AddressMetroStation] = []
    show_metro_only: bool | None = None
    can_edit: bool | None = None


class EmployerRating(BaseType):
    total_rating: str
    reviews_count: int | None = None


class TargetEmployer(BaseType):
    count: int | None = None


class ApplicantServices(BaseType):
    target_employer: TargetEmployer | None = None


class VacancyEmployer(BaseType):
    id: str | None = None
    name: str
    url: str | None = None
    alternate_url: str | None = None
    vacancies_url: str | None = None
    logo_urls: LogoUrls | None = None
    trusted: bool
    accredited_it_employer: bool | None = None
    is_identified_by_esia: bool | None = None
    country_id: int | None = None
    employer_rating: EmployerRating | None = None
    blacklisted: bool | None = None
    applicant_services: ApplicantServices | None = None


class InsiderInterview(BaseType):
    id: str
    url: str


class KeySkill(BaseType):
    name: str


class VacancyLanguage(BaseType):
    id: str
    name: str
    level: IdName


class VacancyTest(BaseType):
    id: str | None = None
    required: bool | None = None


class VideoCoverPicture(BaseType):
    resized_path: str
    resized_width: int
    resized_height: int


class Video(BaseType):
    upload_id: str
    url: str


class VideoVacancy(BaseType):
    cover_picture: VideoCoverPicture | None = None
    video: Video | None = None


class AutoResponse(BaseType):
    accept_auto_response: bool | None = None


class BrandedTemplate(BaseType):
    id: str | None = None
    name: str | None = None


class VacancyManager(BaseType):
    id: str | None = None


class VacancyManagerCounters(BaseType):
    views: int
    responses: int
    unread_responses: int
    resumes_in_progress: int
    invitations: int
    invitations_and_responses: int | None = None
    calls: int | None = None
    new_missed_calls: int | None = None


class VacancyPropertyParameter(BaseType):
    key: str | None = None
    value: str | None = None


class VacancyProperty(BaseType):
    property_type: str
    start_time: datetime | None = None
    end_time: datetime | None = None
    parameters: list[VacancyPropertyParameter] = []


class VacancyPropertiesAppearance(BaseType):
    title: str | None = None
    description: str | None = None


class VacancyProperties(BaseType):
    appearance: VacancyPropertiesAppearance | None = None
    properties: list[VacancyProperty] = []


class BaseVacancy(BaseType):
    id: str
    name: str
    area: AreaLink
    type: IdName
    alternate_url: str
    apply_alternate_url: str
    published_at: datetime
    employer: VacancyEmployer | None = None
    salary_range: SalaryRange | None = None
    address: Address | None = None
    contacts: Contacts | None = None
    department: IdName | None = None
    experience: IdName | None = None
    employment_form: IdName | None = None
    professional_roles: list[IdName] = []
    work_format: list[IdName] | None = None
    work_schedule_by_days: list[IdName] | None = None
    working_hours: list[IdName] | None = None
    fly_in_fly_out_duration: list[IdName] | None = None
    civil_law_contracts: list[IdName] | None = None
    insider_interview: InsiderInterview | None = None
    relations: list[str] = []
    archived: bool | None = None
    has_test: bool
    response_letter_required: bool
    response_url: str | None = None
    accept_incomplete_resumes: bool | None = None
    accept_labor_contract: bool | None = None
    closed_for_applicants: bool | None = None
    show_contacts: bool | None = None
    internship: bool | None = None
    night_shifts: bool | None = None


class VacancySnippet(BaseType):
    requirement: str | None = None
    responsibility: str | None = None


class VacancyCounters(BaseType):
    responses: int | None = None
    total_responses: int | None = None


class VacancyItem(BaseVacancy):
    url: str
    created_at: datetime | None = None
    snippet: VacancySnippet | None = None
    counters: VacancyCounters | None = None
    sort_point_distance: float | None = None
    show_logo_in_search: bool | None = None


class Vacancy(BaseVacancy):
    description: str
    branded_description: str | None = None
    code: str | None = None
    initial_created_at: datetime
    key_skills: list[KeySkill] = []
    languages: list[VacancyLanguage] | None = None
    driver_license_types: list[Id] = []
    age_restriction: IdName | None = None
    billing_type: IdName | None = None
    test: VacancyTest | None = None
    video_vacancy: VideoVacancy | None = None
    auto_response: AutoResponse | None = None
    allow_messages: bool
    approved: bool | None = None
    negotiations_url: str | None = None
    suitable_resumes_url: str | None = None
    inclusiveness_description: str | None = None
    inclusiveness_types: list[str] = []
    hidden: bool | None = None
    archived_at: datetime | None = None
    expires_at: datetime | None = None
    previous_id: str | None = None
    manager: VacancyManager | None = None
    branded_template: BrandedTemplate | None = None
    can_upgrade_billing_type: bool | None = None
    response_notifications: bool | None = None
    counters: VacancyManagerCounters | None = None
    vacancy_properties: VacancyProperties | None = None


class ClusterMetroLine(BaseType):
    id: str
    hex_color: str
    area: AreaLink


class ClusterMetroStation(BaseType):
    id: str
    hex_color: str
    area: AreaLink
    lat: float
    lng: float
    order: int


class ClusterItem(BaseType):
    name: str
    url: str
    count: int
    type: str | None = None
    metro_line: ClusterMetroLine | None = None
    metro_station: ClusterMetroStation | None = None


class Cluster(BaseType):
    id: str
    name: str
    items: list[ClusterItem]


class SearchArgument(BaseType):
    argument: str
    value: str
    disable_url: str
    name: str | None = None
    value_description: str | None = None
    hex_color: str | None = None
    metro_type: str | None = None
    cluster_group: IdName | None = None


class SearchFixes(BaseType):
    fixed: str | None = None
    original: str | None = None


class SearchSuggests(BaseType):
    found: int | None = None
    value: str | None = None


class VacanciesPage(Page[VacancyItem]):
    alternate_url: str | None = None
    clusters: list[Cluster] | None = None
    arguments: list[SearchArgument] | None = None
    fixes: SearchFixes | None = None
    suggests: SearchSuggests | None = None
