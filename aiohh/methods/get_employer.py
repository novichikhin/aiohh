from aiohh.methods.base import BaseMethod
from aiohh.types.employer import Employer


class GetEmployer(BaseMethod[Employer]):
    __returning__ = Employer
    __endpoint__ = "/employers/{employer_id}"

    employer_id: int | str
