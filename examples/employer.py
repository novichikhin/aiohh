import asyncio
import os

from aiohh.api.client import AiohhAPI

USER_AGENT = os.environ["HH_USER_AGENT"]
ACCESS_TOKEN = os.environ["HH_ACCESS_TOKEN"]


async def main() -> None:
    async with AiohhAPI(user_agent=USER_AGENT, access_token=ACCESS_TOKEN) as api:
        me = await api.get_me()

        if me.employer is None:
            print("Token does not belong to an employer")
            return

        vacancies = await api.get_active_vacancies(me.employer.id, per_page=10)

        for vacancy in vacancies.items:
            print(f"{vacancy.name} ({vacancy.alternate_url})")

            negotiations = await api.get_collection_negotiations(
                vacancy.id, show_only_new=True, per_page=20
            )

            for negotiation in negotiations.items:
                resume = negotiation.resume

                if resume is None:
                    continue

                name = " ".join(filter(None, [resume.first_name, resume.last_name]))
                print(f"    {name or 'Anonymous'}: {resume.title}")


if __name__ == "__main__":
    asyncio.run(main())
