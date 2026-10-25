from datetime import date, datetime

from aiohh.types.base import BaseType
from aiohh.types.common import AreaLink, IdName
from aiohh.types.employer import PublicationVariantProperties
from aiohh.types.negotiation import MessageTemplateLink, NegotiationAction
from aiohh.types.vacancy import (
    Address,
    SalaryRange,
    VacancyEmployer,
    VacancyProperties,
    VacancyPropertiesAppearance,
)


class EmployerVacancyManager(BaseType):
    id: str
    first_name: str
    last_name: str
    middle_name: str | None = None


class EmployerVacancyCounters(BaseType):
    views: int | None = None
    responses: int | None = None
    total_responses: int | None = None
    unread_responses: int | None = None
    resumes_in_progress: int | None = None
    invitations: int | None = None
    invitations_and_responses: int | None = None
    calls: int | None = None
    new_missed_calls: int | None = None


class EmployerVacancy(BaseType):
    id: str
    name: str
    url: str
    alternate_url: str
    apply_alternate_url: str
    area: AreaLink
    type: IdName | None = None
    billing_type: IdName | None = None
    employer: VacancyEmployer | None = None
    department: IdName | None = None
    manager: EmployerVacancyManager | None = None
    address: Address | None = None
    salary_range: SalaryRange | None = None
    employment_form: IdName | None = None
    archived: bool
    has_test: bool
    has_updates: bool | None = None
    response_letter_required: bool
    response_url: str | None = None
    closed_for_applicants: bool | None = None
    show_contacts: bool | None = None
    show_logo_in_search: bool | None = None
    can_upgrade_billing_type: bool | None = None
    relations: list[str] = []
    created_at: datetime | None = None
    published_at: datetime
    expires_at: datetime | None = None
    archived_at: datetime | None = None
    sort_point_distance: float | None = None
    counters: EmployerVacancyCounters | None = None
    vacancy_properties: VacancyProperties | None = None
    can_invite: bool | None = None
    negotiations_state: IdName | None = None
    employer_negotiations_state: IdName | None = None
    negotiations_actions: list[NegotiationAction] | None = None
    templates: list[MessageTemplateLink] | None = None


class ProlongationAction(BaseType):
    id: str
    enabled: bool
    method: str | None = None
    url: str | None = None
    disable_reason: IdName | None = None


class VacancyProlongation(BaseType):
    id: str
    expires_at: datetime
    actions: list[ProlongationAction] = []


class UpgradePrice(BaseType):
    amount: str
    currency_code: str


class UpgradeAction(BaseType):
    type: str
    url: str | None = None
    cart_id: int | None = None
    price: UpgradePrice | None = None


class UpgradeBillingType(BaseType):
    id: str
    name: str | None = None
    description: str | None = None


class UpgradeWithoutAction(BaseType):
    reason: str


class VacancyUpgrade(BaseType):
    actions: list[UpgradeAction] = []
    appearance: VacancyPropertiesAppearance | None = None
    vacancy_billing_type: UpgradeBillingType
    vacancy_properties: PublicationVariantProperties | None = None
    without_action: list[UpgradeWithoutAction | None] | None = None


class VacancyUpgrades(BaseType):
    items: list[VacancyUpgrade] = []
    error_reason: str | None = None


class VacancyStatsItem(BaseType):
    date: date
    responses: int | None = None
    views: int | None = None


class VacancyFieldCondition(BaseType):
    required: bool | None = None
    min_length: int | None = None
    max_length: int | None = None
    min_count: int | None = None
    max_count: int | None = None
    min_value: float | None = None
    max_value: float | None = None
    regexp: str | None = None
    fields: dict[str, "VacancyFieldCondition | None"] | None = None


class PreferredNegotiationsOrder(BaseType):
    order_type: IdName
