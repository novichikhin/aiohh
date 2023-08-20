from types import TracebackType
from typing import Optional, Type

from aiohh import __version__
from aiohh.api.base import (
    BaseAPI,
    HH_OAUTH_TOKEN_HEADER_KEY,
    HH_USER_AGENT_HEADER_KEY,
    HH_OAUTH_TOKEN_HEADER_VALUE,
    HH_USER_AGENT_HEADER_VALUE
)
from aiohh.client.session.aiohttp import AiohttpSession
from aiohh.client.session.base import BaseSession, Session
from aiohh.methods.base import BaseMethod, ReturningType
from aiohh.methods import (
    GetVacancy
)
from aiohh.types import (
    Vacancy
)


class AiohhAPI(BaseAPI):

    def __init__(
        self,
        *,
        oauth_token: str,
        email: str,
        session: Optional[BaseSession[Session]] = None
    ):
        self._headers = {
            HH_OAUTH_TOKEN_HEADER_KEY: HH_OAUTH_TOKEN_HEADER_VALUE.format(
                oauth_token=oauth_token
            ),
            HH_USER_AGENT_HEADER_KEY: HH_USER_AGENT_HEADER_VALUE.format(
                version=__version__,
                email=email
            )
        }

        self._session = session

        if self._session is None:
            self._session = AiohttpSession()

    async def __aenter__(self) -> "AiohhAPI":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> None:
        if self._session is not None:
            await self._session.close()

    async def __call__(
        self,
        method: BaseMethod[ReturningType]
    ) -> ReturningType:
        return await self._session(method=method, headers=self._headers)

    async def get_vacancy(self, vacancy_id: int) -> Vacancy:
        return await self(method=GetVacancy(vacancy_id=vacancy_id))
