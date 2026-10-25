from datetime import datetime

from aiohh.types.base import BaseType
from aiohh.types.common import AreaLink, Id, IdName
from aiohh.types.employer import EmployerShort, PublicationVariantProperties
from aiohh.types.vacancy import (
    Address,
    AutoResponse,
    BrandedTemplate,
    Contacts,
    KeySkill,
    SalaryRange,
    VacancyLanguage,
    VacancyManager,
    VacancyPropertiesAppearance,
    VacancyTest,
)


class DraftValidationError(BaseType):
    value: str
    reason: str | None = None


class DraftResponse(BaseType):
    id: str
    name: str
    publication_ready: bool
    ignored_fields: list[str] = []
    validation_errors: list[DraftValidationError] = []


class DraftPublication(BaseType):
    count: int
    billing_type: IdName | None = None
    appearance: VacancyPropertiesAppearance | None = None
    vacancy_properties: PublicationVariantProperties | None = None


class DraftAutoPublication(BaseType):
    bill_uid: str
    cart_id: str


class DraftMeta(BaseType):
    draft_id: str
    publication_ready: bool
    completed_fields_percentage: int
    last_change_time: datetime | None = None
    scheduled_at: datetime | None = None
    auto_publication: DraftAutoPublication | None = None
    ignored_fields: list[str] | None = None
    validation_errors: list[DraftValidationError] | None = None
    required_publications: list[DraftPublication] | None = None
    insufficient_publications: list[DraftPublication] | None = None
    insufficient_quotas: list[DraftPublication] | None = None


class DraftAssignedManager(BaseType):
    id: str | None = None
    full_name: str | None = None


class DraftVacancyProperty(BaseType):
    property_type: str
    parameters: list[str] = []


class DraftVacancyProperties(BaseType):
    appearance: VacancyPropertiesAppearance | None = None
    properties: list[DraftVacancyProperty] = []


class VacancyDraftItem(DraftMeta):
    url: str
    name: str | None = None
    areas: list[AreaLink] = []
    billing_type: IdName | None = None
    assigned_manager: DraftAssignedManager | None = None
    auto_response: AutoResponse | None = None
    closed_for_applicants: bool | None = None
    vacancy_properties: DraftVacancyProperties | None = None


class VacancyDraft(BaseType):
    name: str | None = None
    description: str | None = None
    code: str | None = None
    employer: EmployerShort | None = None
    custom_employer_name: str | None = None
    department: IdName | None = None
    manager: VacancyManager | None = None
    assigned_manager: DraftAssignedManager | None = None
    areas: list[AreaLink] = []
    address: Address | None = None
    contacts: Contacts | None = None
    salary_range: SalaryRange | None = None
    type: IdName | None = None
    billing_type: IdName | None = None
    experience: IdName | None = None
    employment_form: IdName | None = None
    work_format: list[IdName] | None = None
    work_schedule_by_days: list[IdName] | None = None
    working_hours: list[IdName] | None = None
    fly_in_fly_out_duration: list[IdName] | None = None
    civil_law_contracts: list[IdName] | None = None
    professional_roles: list[IdName] = []
    key_skills: list[KeySkill] = []
    languages: list[VacancyLanguage] = []
    driver_license_types: list[Id] = []
    age_restriction: IdName | None = None
    branded_template: BrandedTemplate | None = None
    test: VacancyTest | None = None
    has_test: bool | None = None
    auto_response: AutoResponse | None = None
    allow_messages: bool | None = None
    response_url: str | None = None
    response_letter_required: bool | None = None
    response_notifications: bool | None = None
    accept_incomplete_resumes: bool | None = None
    accept_labor_contract: bool | None = None
    closed_for_applicants: bool | None = None
    internship: bool | None = None
    night_shifts: bool | None = None
    inclusiveness_description: str | None = None
    inclusiveness_types: list[str] = []
    employer_service_id: str | None = None
    vacancy_properties: DraftVacancyProperties | None = None
    meta_info: DraftMeta


class VacancyDuplicates(BaseType):
    found: int
    has_duplicates: bool
    items: list[int] = []


class PublishedDraft(BaseType):
    vacancy_ids: list[int] = []
