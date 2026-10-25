from aiohh.enums.webhook_action_type import WebhookActionType
from aiohh.types.base import BaseType


class WebhookActionSettings(BaseType):
    vacancies_only_mine: bool | None = None


class WebhookAction(BaseType):
    type: WebhookActionType | str
    settings: WebhookActionSettings | None = None


class WebhookSubscription(BaseType):
    id: str
    url: str
    actions: list[WebhookAction] = []
