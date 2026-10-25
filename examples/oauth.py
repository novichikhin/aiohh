import asyncio
import os
import secrets

from aiohh.api.client import AiohhAPI
from aiohh.exceptions.api import ForbiddenError
from aiohh.utils.oauth import (
    build_authorization_url,
    create_code_challenge,
    generate_code_verifier,
)

USER_AGENT = os.environ["HH_USER_AGENT"]
CLIENT_ID = os.environ["HH_CLIENT_ID"]
CLIENT_SECRET = os.environ["HH_CLIENT_SECRET"]


async def main() -> None:
    code_verifier = generate_code_verifier()

    print(
        build_authorization_url(
            CLIENT_ID,
            state=secrets.token_urlsafe(16),
            code_challenge=create_code_challenge(code_verifier),
        )
    )

    code = input("Code from redirect: ")

    async with AiohhAPI(user_agent=USER_AGENT) as api:
        token = await api.get_user_token(
            CLIENT_ID, CLIENT_SECRET, code, code_verifier=code_verifier
        )
        api.access_token = token.access_token

        try:
            me = await api.get_me()
        except ForbiddenError as error:
            if error.oauth_error != "token-expired":
                raise

            token = await api.refresh_user_token(token.refresh_token)
            api.access_token = token.access_token
            me = await api.get_me()

        print(me.first_name, me.last_name)

        vacancies = await api.search_vacancies(text="python", area=[1], per_page=10)

        for vacancy in vacancies.items:
            print(vacancy.name, vacancy.alternate_url)


if __name__ == "__main__":
    asyncio.run(main())
