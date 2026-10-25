from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.webhook import WebhookAction


class UpdateWebhookSubscription(BaseMethod[None]):
    __returning__ = None
    __http_method__ = HTTPMethod.PUT
    __endpoint__ = "/webhook/subscriptions/{subscription_id}"

    subscription_id: int | str
    url: str | None = None
    actions: list[WebhookAction] | None = None
