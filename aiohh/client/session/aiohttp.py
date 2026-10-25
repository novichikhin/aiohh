import asyncio

import aiohttp

from aiohh.client.session.base import (
    DEFAULT_API_URL,
    DEFAULT_TIMEOUT,
    BaseSession,
    Request,
    Response,
)
from aiohh.exceptions.network import NetworkError


class AiohttpSession(BaseSession):
    def __init__(
        self, api_url: str = DEFAULT_API_URL, timeout: float = DEFAULT_TIMEOUT
    ) -> None:
        super().__init__(api_url=api_url, timeout=timeout)

        self._session: aiohttp.ClientSession | None = None

    async def create_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            )

        return self._session

    async def send(self, request: Request) -> Response:
        session = await self.create_session()

        try:
            async with session.request(
                method=request.http_method.value,
                url=request.url,
                headers=request.headers,
                params=request.params,
                json=request.json,
                data=request.data,
            ) as response:
                return Response(
                    status_code=response.status, content=await response.read()
                )
        except (asyncio.TimeoutError, aiohttp.ClientError) as error:
            raise NetworkError(
                f"Request to {request.url} failed: {type(error).__name__}: {error}"
            ) from error

    async def close(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()
