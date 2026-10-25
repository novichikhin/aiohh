from aiohh.methods.base import BaseMethod
from aiohh.types.resume import Resume


class GetResume(BaseMethod[Resume]):
    __returning__ = Resume
    __endpoint__ = "/resumes/{resume_id}"

    resume_id: str
    with_negotiations_history: bool | None = None
    with_creds: bool | None = None
    with_job_search_status: bool | None = None
