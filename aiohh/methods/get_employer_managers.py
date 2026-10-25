from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.manager import EmployerManagerItem


class GetEmployerManagers(BaseMethod[Page[EmployerManagerItem]]):
    __returning__ = Page[EmployerManagerItem]
    __endpoint__ = "/employers/{employer_id}/managers"

    employer_id: int | str
    search_text: str | None = None
    page: int | None = None
    per_page: int | None = None
