import asyncio
import os
from collections.abc import AsyncIterator

from aiohh.api.client import AiohhAPI
from aiohh.types.vacancy import VacancyItem

USER_AGENT = os.environ["HH_USER_AGENT"]
ACCESS_TOKEN = os.environ["HH_ACCESS_TOKEN"]
PER_PAGE = 100
MAX_PAGES = 5


async def iter_vacancies(api: AiohhAPI, text: str) -> AsyncIterator[VacancyItem]:
    page = 0

    while page < MAX_PAGES:
        result = await api.search_vacancies(text=text, page=page, per_page=PER_PAGE)

        for vacancy in result.items:
            yield vacancy

        page += 1

        if page >= result.pages:
            break


async def main() -> None:
    async with AiohhAPI(user_agent=USER_AGENT, access_token=ACCESS_TOKEN) as api:
        vacancy_ids = [
            vacancy.id async for vacancy in iter_vacancies(api, "python developer")
        ]
        print(f"Found {len(vacancy_ids)} vacancies")

        vacancies = await asyncio.gather(
            *(api.get_vacancy(vacancy_id) for vacancy_id in vacancy_ids[:5])
        )

        for vacancy in vacancies:
            skills = ", ".join(skill.name for skill in vacancy.key_skills)
            print(vacancy.name, "|", skills or "no skills")


if __name__ == "__main__":
    asyncio.run(main())
