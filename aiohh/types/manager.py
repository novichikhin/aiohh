from datetime import datetime

from aiohh.types.base import BaseType
from aiohh.types.common import AreaLink, IdName
from aiohh.types.vacancy import BrandedTemplate


class ManagerAccountEmployer(BaseType):
    id: str | None = None
    name: str | None = None


class ManagerAccount(BaseType):
    id: str | None = None
    employer: ManagerAccountEmployer


class ManagerAccounts(BaseType):
    items: list[ManagerAccount]
    primary_account_id: str
    current_account_id: str | None = None
    is_primary_account_blocked: bool


class ManagerPhone(BaseType):
    country: str
    city: str
    number: str
    formatted: str | None = None
    comment: str | None = None


class EmployerManagerItem(BaseType):
    id: str
    email: str
    position: str
    area: AreaLink | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    full_name: str | None = None
    is_main_contact_person: bool | None = None
    phone: ManagerPhone | None = None
    additional_phone: ManagerPhone | None = None
    special_note_1: str | None = None
    special_note_2: str | None = None
    vacancies_count: int | None = None


class EmployerManager(EmployerManagerItem):
    creation_time: datetime | None = None
    manager_type: IdName | None = None
    permissions: list[IdName] = []


class ManagerType(IdName):
    available_permissions: list[IdName] = []


class ResumeViewLimit(BaseType):
    resume_view: int
    resume_view_from_api: int | None = None


class ManagerResumeLimits(BaseType):
    limits: ResumeViewLimit
    spend: ResumeViewLimit
    left: ResumeViewLimit


class ManagerSettingsCurrency(BaseType):
    code: str
    abbr: str
    name: str


class ManagerSettings(BaseType):
    default_currency: ManagerSettingsCurrency
    default_vacancy_branded_template: BrandedTemplate | None = None
    use_sms_notification: bool
