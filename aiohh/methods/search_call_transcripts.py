from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.call import CallTranscripts


class SearchCallTranscripts(BaseMethod[CallTranscripts]):
    __returning__ = CallTranscripts
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/calls/transcripts/search"

    call_ids: list[str] | None = None
    link_ids: list[str] | None = None
