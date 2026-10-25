from typing import Literal

from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.employer import EmployerItem


class SearchEmployers(BaseMethod[Page[EmployerItem]]):
    __returning__ = Page[EmployerItem]
    __endpoint__ = "/employers"

    text: str | None = None
    area: list[int | str] | None = None
    type: list[str] | None = None
    only_with_vacancies: bool | None = None
    sort_by: Literal["by_name", "by_vacancies_open"] | None = None
    page: int | None = None
    per_page: int | None = None
