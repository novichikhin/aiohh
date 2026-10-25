from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class DeleteApplicantComment(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.DELETE
    __endpoint__ = "/applicant_comments/{applicant_id}/{comment_id}"

    applicant_id: int | str
    comment_id: int | str
