from datetime import date

from aiohh.types.base import BaseType
from aiohh.types.common import IdName


class ClickmeStatisticsItem(BaseType):
    campaign_id: str
    campaign_title: str
    campaign_type: str
    clickme_account_id: str
    clickme_account_title: str | None = None
    banner_id: str | None = None
    banner_title: str | None = None
    vacancy_id: str
    vacancy_title: str
    vacancy_area_name: str
    url: str
    amount: float
    clicks: int
    impressions: int
    responses: int
    before_clickme_responses: int
    after_clickme_responses: int
    date_create: date
    date_start: date
    date_end: date
    date_archive: date | None = None


class IdNameDescription(IdName):
    description: str


class SalaryProfessionalArea(IdName):
    specializations: list[IdNameDescription] = []


class SalaryArea(IdName):
    areas: list["SalaryArea"] = []


class MarketSalary(BaseType):
    bottom: float
    median: float
    upper: float
    average: float | None = None
    minimum: float | None = None
    maximum: float | None = None


class IndirectCalculation(BaseType):
    indirect_regional_ratio: float
    indirect_areas: list[IdName] | None = None
    indirect_employee_levels: list[IdName] | None = None


class SalaryResultingParameters(BaseType):
    areas: list[IdName] = []
    excluded_areas: list[IdName] | None = None
    employee_levels: list[IdName] | None = None
    industries: list[IdName] | None = None
    specialities: list[IdName] | None = None
    sources: list[str] = []
    employers_count: int
    positions_count: int
    indirect_calculation: IndirectCalculation | None = None


class SalaryEvaluation(BaseType):
    market_salary: MarketSalary
    resulting_parameters: SalaryResultingParameters
