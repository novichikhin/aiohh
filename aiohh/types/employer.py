from datetime import datetime

from aiohh.types.base import BaseType
from aiohh.types.common import AreaLink, IdName, LogoUrls
from aiohh.types.vacancy import (
    AddressMetroStation,
    ApplicantServices,
    VacancyPropertiesAppearance,
    VacancyPropertyParameter,
)


class EmployerShort(BaseType):
    id: str
    name: str
    url: str
    alternate_url: str
    logo_urls: LogoUrls | None = None


class EmployerItem(BaseType):
    id: str
    name: str
    url: str
    alternate_url: str
    vacancies_url: str
    logo_urls: LogoUrls | None = None
    open_vacancies: int | None = None
    is_identified_by_esia: bool | None = None


class EmployerInsiderInterview(BaseType):
    id: str
    title: str
    url: str


class BrandingPicture(BaseType):
    resized_path: str


class BrandingWidgetItem(BaseType):
    picture_id: int
    resized_path: str


class BrandingWidget(BaseType):
    type: str
    items: list[BrandingWidgetItem] = []


class BrandingConstructor(BaseType):
    url: str
    header_picture: BrandingPicture | None = None
    widgets: list[BrandingWidget] = []


class BrandingMakeupHeaderPicture(BaseType):
    web_path: str | None = None
    mob_app_path: str | None = None


class BrandingMakeup(BaseType):
    url: str
    header_picture: BrandingMakeupHeaderPicture | None = None


class EmployerBranding(BaseType):
    type: str | None = None
    constructor: BrandingConstructor | None = None
    makeup: BrandingMakeup | None = None
    template_code: str | None = None
    template_version_id: str | None = None


class Employer(BaseType):
    id: str
    name: str
    type: str | None = None
    description: str | None = None
    site_url: str | None = None
    alternate_url: str
    vacancies_url: str
    area: AreaLink
    logo_urls: LogoUrls | None = None
    industries: list[IdName] = []
    insider_interviews: list[EmployerInsiderInterview] = []
    relations: list[str] = []
    trusted: bool
    accredited_it_employer: bool | None = None
    is_identified_by_esia: bool | None = None
    open_vacancies: int | None = None
    country_code: str | None = None
    applicant_services: ApplicantServices | None = None
    branding: EmployerBranding | None = None


class AddressManager(BaseType):
    id: str | None = None
    full_name: str | None = None


class EmployerAddress(BaseType):
    id: str | None = None
    city: str | None = None
    street: str | None = None
    building: str | None = None
    description: str | None = None
    raw: str | None = None
    lat: float | None = None
    lng: float | None = None
    metro_stations: list[AddressMetroStation] = []
    manager: AddressManager | None = None
    can_edit: bool | None = None
    deleted: bool | None = None


class VacancyBrandedTemplateItem(IdName):
    version_id: str | None = None


class ServiceBalance(BaseType):
    actual: int
    initial: int


class EmployerService(BaseType):
    id: str
    service_type: IdName
    activated_at: datetime
    expires_at: datetime
    balance: ServiceBalance | None = None


class MethodAccessStatus(BaseType):
    has_access: bool


class MethodAccess(BaseType):
    id: str
    description: str
    access: MethodAccessStatus


class PriceRegion(BaseType):
    id: str | None = None
    title: str | None = None
    areas_url: str | None = None


class ProfessionalRoleGroup(BaseType):
    id: str | None = None
    title: str | None = None


class SuitablePackage(BaseType):
    count: int
    employer_service_id: str | None = None
    expiration_time: datetime | None = None
    included_properties: list[str] = []
    invalid: bool
    price_regions: list[PriceRegion] | None = None
    prof_role_group: list[ProfessionalRoleGroup] | None = None


class RequiredVacancyProperty(BaseType):
    property_type: str
    parameters: list[VacancyPropertyParameter] | None = None


class PublicationVariantProperties(BaseType):
    required: list[RequiredVacancyProperty] = []


class PublicationVariant(BaseType):
    appearance: VacancyPropertiesAppearance
    available_publications_count: int
    suitable_packages: list[SuitablePackage] | None = None
    vacancy_properties: PublicationVariantProperties


class AvailablePublications(BaseType):
    publication_variants: list[PublicationVariant] = []
