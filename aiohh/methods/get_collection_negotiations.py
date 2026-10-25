from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import NegotiationsPage


class GetCollectionNegotiations(BaseMethod[NegotiationsPage]):
    __returning__ = NegotiationsPage
    __endpoint__ = "/negotiations/{collection_name}"

    vacancy_id: int | str
    collection_name: str = "response"
    search_text: str | None = None
    age_from: int | None = None
    age_to: int | None = None
    area: list[int | str] | None = None
    citizenship: list[int | str] | None = None
    currency: str | None = None
    salary_from: int | None = None
    salary_to: int | None = None
    driver_license_types: list[str] | None = None
    educational_institution: list[int | str] | None = None
    education_level: str | None = None
    experience: list[str] | None = None
    gender: str | None = None
    language: list[str] | None = None
    relocation: str | None = None
    search_radius_meters: int | None = None
    show_only_new: bool | None = None
    show_only_new_responses: bool | None = None
    show_only_with_vehicle: bool | None = None
    show_only_with_medical_book: bool | None = None
    show_only_with_self_employment: bool | None = None
    order_by: str | None = None
    page: int | None = None
    per_page: int | None = None
