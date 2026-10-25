from datetime import datetime

from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.employer import EmployerAddress


class GetEmployerAddresses(BaseMethod[Page[EmployerAddress]]):
    __returning__ = Page[EmployerAddress]
    __endpoint__ = "/employers/{employer_id}/addresses"

    employer_id: int | str
    changed_after: datetime | None = None
    manager_id: int | str | None = None
    with_manager: bool | None = None
    page: int | None = None
    per_page: int | None = None
