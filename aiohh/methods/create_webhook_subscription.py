from aiohh.enums.http_method import HTTPMethod
from aiohh.methods.base import BaseMethod
from aiohh.types.common import Id
from aiohh.types.webhook import WebhookAction


class CreateWebhookSubscription(BaseMethod[Id]):
    __returning__ = Id
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/webhook/subscriptions"

    url: str
    actions: list[WebhookAction]
