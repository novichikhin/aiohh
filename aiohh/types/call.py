from datetime import datetime

from aiohh.types.base import BaseType


class CallParticipantInfo(BaseType):
    role: str
    client: str
    first_name: str | None = None
    last_name: str | None = None
    real_phone: str | None = None
    virtual_phone: str | None = None
    employer_manager_id: str | None = None


class CallContext(BaseType):
    voicemail_detected: bool
    chat_id: str | None = None
    employer_id: str | None = None
    resume_id: str | None = None
    topic_id: str | None = None
    vacancy_id: str | None = None


class Call(BaseType):
    id: str
    start_date_time: datetime
    successful: bool
    duration_seconds: int | None = None
    caller_info: CallParticipantInfo
    recipient_info: CallParticipantInfo
    context: CallContext


class CallsHistory(BaseType):
    calls: list[Call] = []
    total: int
    next_cursor: str | None = None
    previous_cursor: str | None = None


class CallLink(BaseType):
    link: str
    link_id: str
    qr_code: str
    expires_at: datetime


class CallTranscript(BaseType):
    status: str
    transcript_url: str | None = None
    expires_at: datetime | None = None


class CallTranscripts(BaseType):
    transcripts: dict[str, CallTranscript] = {}
