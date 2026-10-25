from aiohh.methods.base import BaseMethod
from aiohh.types.common import Page
from aiohh.types.negotiation import ApplicantComment


class GetApplicantComments(BaseMethod[Page[ApplicantComment]]):
    __returning__ = Page[ApplicantComment]
    __endpoint__ = "/applicant_comments/{applicant_id}"

    applicant_id: int | str
    order_by: str | None = None
    page: int | None = None
    per_page: int | None = None
