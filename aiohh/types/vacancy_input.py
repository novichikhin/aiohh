from pydantic import Field

from aiohh.types.base import BaseType
from aiohh.types.common import Id


class SalaryRangeInput(BaseType):
    currency: str
    gross: bool
    from_: int | None = Field(default=None, alias="from")
    to: int | None = None
    frequency: Id | None = None
    mode: Id


class VacancyAddressInput(BaseType):
    id: str | None = None
    show_metro_only: bool | None = None


class VacancyLanguageInput(BaseType):
    id: str
    level: Id


class VacancyPropertyInput(BaseType):
    property_type: str


class VacancyPropertiesInput(BaseType):
    properties: list[VacancyPropertyInput]
