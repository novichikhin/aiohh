import asyncio
import os

from aiohh.api.client import AiohhAPI
from aiohh.exceptions.api import APIError

USER_AGENT = os.environ["HH_USER_AGENT"]


async def main() -> None:
    async with AiohhAPI(user_agent=USER_AGENT) as api:
        areas = await api.suggest_areas("Моск")

        for area in areas.items:
            print(area.id, area.text)

        dictionaries = await api.get_dictionaries()

        for experience in dictionaries.experience:
            print(experience.id, experience.name)

        try:
            page = await api.get_similar_vacancies(84190497, per_page=5)
        except APIError as error:
            print(error)
            return

        for vacancy in page.items:
            print(vacancy.name, vacancy.salary_range)


if __name__ == "__main__":
    asyncio.run(main())
