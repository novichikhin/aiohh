import asyncio
from typing import Any, Mapping

import aiohttp

from aiohh.client.session.base import BaseSession
from aiohh.exceptions.network import NetworkError
from aiohh.methods.base import BaseMethod, ReturningType


class AiohttpSession(BaseSession[aiohttp.ClientSession]):

    def create(self) -> aiohttp.ClientSession:
        if self.is_invalid:
            self._session = aiohttp.ClientSession()

        return self._session

    async def close(self) -> None:
        if not self.is_invalid:
            await self._session.close()

    async def __call__(
        self,
        method: BaseMethod[ReturningType],
        headers: Mapping[str, Any]
    ) -> ReturningType:
        self._session = self.create()
        request = self._build_request(method=method, headers=headers)

        try:
            async with self._session.request(
                method=request.http_method,
                url=request.url,
                headers=request.headers
            ) as response:
                built_response = self._build_response(
                    status_code=response.status,
                    body=await response.read(),
                    headers=response.headers,
                    content_type=response.content_type
                )
        except (asyncio.TimeoutError, aiohttp.ClientError):
            raise NetworkError

        return self._parse_response(method=method, response=built_response)

    @property
    def is_invalid(self) -> bool:
        return self._session is None or self._session.closed
