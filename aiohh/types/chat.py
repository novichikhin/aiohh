from datetime import datetime

from aiohh.types.base import BaseType


class ChatDisplay(BaseType):
    title: str
    icon: str | None = None


class ChatSenderDisplay(BaseType):
    name: str
    icon: str | None = None
    role: str | None = None
    is_current_participant: bool


class ChatAttachmentPreview(BaseType):
    url: str | None = None


class ChatAttachment(BaseType):
    title: str
    url: str
    content_type: str
    preview: ChatAttachmentPreview | None = None


class ChatParticipantShort(BaseType):
    id: str
    name: str
    icon: str | None = None


class ChatMessagePayload(BaseType):
    text: str | None = None
    attachments: list[ChatAttachment] | None = None
    moved_participant: ChatParticipantShort | None = None


class ChatMessage(BaseType):
    id: str
    type: str | None = None
    creation_time: datetime
    last_change_time: datetime | None = None
    can_edit: bool | None = None
    sender_participant_id: str
    sender_display_info: ChatSenderDisplay
    viewed_by_opponent: bool | None = None
    payload: ChatMessagePayload


class BaseChat(BaseType):
    id: str
    type: str
    display: ChatDisplay
    creation_time: datetime
    muted: bool
    unread_message_count: int
    block_reason: str | None = None
    vacancy_id: str | None = None


class Chat(BaseChat):
    last_message: ChatMessage | None = None


class ChatState(BaseType):
    allowed: bool
    reason: str | None = None


class ChatStates(BaseType):
    send_file_state: ChatState
    write_message_state: ChatState


class ChatMessages(BaseChat):
    messages: list[ChatMessage] = []
    has_more: bool
    chat_states: ChatStates


class UnreadChatsCount(BaseType):
    unread_chats_count: int


class ChatParticipant(BaseType):
    id: str
    name: str
    icon: str | None = None
    role: str | None = None
    type: str | None = None
    resume_id: str | None = None
    last_viewed_message_id: str | None = None


class ChatFileUploadLink(BaseType):
    upload_url: str
    expires_at: datetime


class ChatFilesUpload(BaseType):
    max_size: int
    mime_type: list[str] = []
    type: list[str] = []


class ChatFilesConditions(BaseType):
    files_upload: ChatFilesUpload
