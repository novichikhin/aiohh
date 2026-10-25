from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class UpdateApplicantComment(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/applicant_comments/{applicant_id}/{comment_id}"
    __body_format__ = BodyFormat.FORM

    applicant_id: int | str
    comment_id: int | str
    text: str | None = None
    access_type: str | None = None
