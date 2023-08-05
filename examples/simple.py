import asyncio

from aiohh.api.client import AiohhAPI
from aiohh.client.session.aiohttp import AiohttpSession
from aiohh.exceptions.api import APIError


async def example_custom_session() -> None:
    session = AiohttpSession()
    aiohh = AiohhAPI(
        oauth_token="Test",
        email="novichixinn@gmail.com",
        session=session
    )

    try:
        vacancy = await aiohh.get_vacancy(vacancy_id=84190497)

        print(vacancy.name)
    except APIError as err:
        print(err.status_code, err.detailed_errors)
    finally:
        await session.close()


async def example_simple() -> None:
    aiohh: AiohhAPI
    async with AiohhAPI(
        oauth_token="Test",
        email="novichixinn@gmail.com"
    ) as aiohh:
        try:
            vacancy = await aiohh.get_vacancy(vacancy_id=84190497)

            print(vacancy.name)
        except APIError as err:
            print(err.status_code, err.detailed_errors)


async def main() -> None:
    tasks = [
        asyncio.create_task(example_custom_session()),
        asyncio.create_task(example_simple())
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
