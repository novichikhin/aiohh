from aiohh.methods.base import BaseMethod
from aiohh.types.resume import NegotiationsHistory


class GetResumeNegotiationsHistory(BaseMethod[NegotiationsHistory]):
    __returning__ = NegotiationsHistory
    __endpoint__ = "/resumes/{resume_id}/negotiations_history"

    resume_id: str
