import asyncio
import os

from aiohh.api.client import AiohhAPI
from aiohh.enums.webhook_action_type import WebhookActionType
from aiohh.types.webhook import WebhookAction

USER_AGENT = os.environ["HH_USER_AGENT"]
ACCESS_TOKEN = os.environ["HH_ACCESS_TOKEN"]
WEBHOOK_URL = os.environ["HH_WEBHOOK_URL"]


async def main() -> None:
    async with AiohhAPI(user_agent=USER_AGENT, access_token=ACCESS_TOKEN) as api:
        subscription = await api.create_webhook_subscription(
            WEBHOOK_URL,
            actions=[
                WebhookAction(type=WebhookActionType.NEW_NEGOTIATION_VACANCY),
                WebhookAction(type=WebhookActionType.CHAT_MESSAGE_CREATED),
            ],
        )
        print(f"Created subscription {subscription.id}")

        subscriptions = await api.get_webhook_subscriptions()

        for item in subscriptions.items:
            print(item.id, item.url, [action.type for action in item.actions])

        await api.delete_webhook_subscription(subscription.id)
        print(f"Deleted subscription {subscription.id}")


if __name__ == "__main__":
    asyncio.run(main())
