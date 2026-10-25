from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.negotiation import ApplicantComment


class AddApplicantComment(BaseMethod[ApplicantComment]):
    __returning__ = ApplicantComment
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/applicant_comments/{applicant_id}"
    __body_format__ = BodyFormat.FORM

    applicant_id: int | str
    text: str
    access_type: str
