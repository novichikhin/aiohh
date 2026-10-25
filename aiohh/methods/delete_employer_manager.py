from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class DeleteEmployerManager(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.DELETE
    __endpoint__ = "/employers/{employer_id}/managers/{manager_id}"

    employer_id: int | str
    manager_id: int | str
    successor_id: int | str
