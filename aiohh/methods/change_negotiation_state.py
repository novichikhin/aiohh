from aiohh.enums.body_format import BodyFormat
from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod


class ChangeNegotiationState(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/negotiations/{collection_name}/{negotiation_id}"
    __body_format__ = BodyFormat.FORM

    collection_name: str
    negotiation_id: int | str
    message: str | None = None
    send_sms: bool | None = None
    address_id: int | str | None = None
