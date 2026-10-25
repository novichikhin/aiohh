from aiohh.methods.base import BaseMethod
from aiohh.types.statistics import SalaryEvaluation


class GetSalaryEvaluation(BaseMethod[SalaryEvaluation]):
    __returning__ = SalaryEvaluation
    __endpoint__ = "/salary_statistics/paid/salary_evaluation/{area_id}"

    area_id: int | str
    exclude_area: list[int | str] | None = None
    employee_level: list[int | str] | None = None
    industry: list[int | str] | None = None
    speciality: list[int | str] | None = None
    position_name: str | None = None
    extend_sources: bool | None = None
