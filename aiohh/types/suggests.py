from aiohh.types.base import BaseType
from aiohh.types.common import IdName, Items, LogoUrls


class SuggestProfessionalRole(IdName):
    accept_incomplete_resumes: bool


class Specialization(IdName):
    profarea_id: str
    profarea_name: str


class PositionSuggest(BaseType):
    id: str
    text: str
    professional_roles: list[SuggestProfessionalRole] = []
    specializations: list[Specialization] | None = None


class VacancyPositionSuggest(BaseType):
    id: str
    text: str
    professional_roles: list[SuggestProfessionalRole] = []


class AreaSuggest(BaseType):
    id: str
    text: str
    url: str
    parent: "AreaSuggest | None" = None


class FieldOfStudySuggest(BaseType):
    id: str
    text: str


class ProfessionalRoleSuggest(BaseType):
    id: str
    text: str
    accept_incomplete_resumes: bool


class KeywordSuggest(BaseType):
    text: str


class KeywordSuggests(Items[KeywordSuggest]):
    suggest_id: str | None = None


class CompanySuggest(BaseType):
    id: str
    text: str
    url: str | None = None
    area: IdName
    logo_urls: LogoUrls | None = None
    industries: list[IdName] | None = None
