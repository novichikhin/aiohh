import json
from collections.abc import AsyncIterator
from pathlib import Path
from typing import Any

import pytest

from aiohh.api.client import AiohhAPI
from aiohh.client.session.base import BaseSession, Request, Response

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> bytes:
    return (FIXTURES / name).read_bytes()


class FakeSession(BaseSession):
    def __init__(self) -> None:
        super().__init__()

        self.requests: list[Request] = []
        self.responses: list[Response] = []
        self.closed = False

    def add_response(self, content: Any = None, status_code: int = 200) -> None:
        if content is None:
            body = b""
        elif isinstance(content, bytes):
            body = content
        else:
            body = json.dumps(content).encode()

        self.responses.append(Response(status_code=status_code, content=body))

    async def send(self, request: Request) -> Response:
        self.requests.append(request)

        return self.responses.pop(0)

    async def close(self) -> None:
        self.closed = True


@pytest.fixture
def session() -> FakeSession:
    return FakeSession()


@pytest.fixture
async def api(session: FakeSession) -> AsyncIterator[AiohhAPI]:
    async with AiohhAPI(
        user_agent="aiohh-tests/1.0 (tests@example.com)", session=session
    ) as api:
        yield api
