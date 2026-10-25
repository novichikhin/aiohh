from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.webhook import WebhookSubscription


class GetWebhookSubscriptions(BaseMethod[Items[WebhookSubscription]]):
    __returning__ = Items[WebhookSubscription]
    __endpoint__ = "/webhook/subscriptions"
