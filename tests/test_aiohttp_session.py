import asyncio
import json
from collections.abc import AsyncIterator

import pytest
from aiohttp import web
from aiohttp.test_utils import TestServer

from aiohh.client.session.aiohttp import AiohttpSession
from aiohh.client.session.base import Request
from aiohh.enums.http_method import HTTPMethod
from aiohh.exceptions.network import NetworkError


async def echo(request: web.Request) -> web.Response:
    return web.json_response(
        {
            "method": request.method,
            "path": request.path,
            "query": [[name, value] for name, value in request.query.items()],
            "headers": {"HH-User-Agent": request.headers.get("HH-User-Agent")},
            "content_type": request.content_type,
            "body": await request.text(),
        },
        status=201,
    )


async def slow(request: web.Request) -> web.Response:
    await asyncio.sleep(1)

    return web.Response()


@pytest.fixture
async def server() -> AsyncIterator[TestServer]:
    app = web.Application()
    app.router.add_get("/slow", slow)
    app.router.add_route("*", "/{path:.*}", echo)

    server = TestServer(app)
    await server.start_server()

    yield server

    await server.close()


@pytest.fixture
async def session(server: TestServer) -> AsyncIterator[AiohttpSession]:
    session = AiohttpSession(api_url=str(server.make_url("")), timeout=0.2)

    yield session

    await session.close()


async def test_send_get(server: TestServer, session: AiohttpSession) -> None:
    response = await session.send(
        Request(
            http_method=HTTPMethod.GET,
            url=str(server.make_url("/vacancies")),
            headers={"HH-User-Agent": "test"},
            params=[("area", "1"), ("area", "2"), ("text", "python")],
        )
    )

    payload = json.loads(response.content)

    assert response.status_code == 201
    assert payload["query"] == [["area", "1"], ["area", "2"], ["text", "python"]]
    assert payload["headers"] == {"HH-User-Agent": "test"}


async def test_send_form(server: TestServer, session: AiohttpSession) -> None:
    response = await session.send(
        Request(
            http_method=HTTPMethod.POST,
            url=str(server.make_url("/token")),
            data=[("topic_id", "1"), ("topic_id", "2")],
        )
    )

    payload = json.loads(response.content)

    assert payload["content_type"] == "application/x-www-form-urlencoded"
    assert payload["body"] == "topic_id=1&topic_id=2"


async def test_send_json(server: TestServer, session: AiohttpSession) -> None:
    response = await session.send(
        Request(
            http_method=HTTPMethod.PUT,
            url=str(server.make_url("/vacancies/1")),
            json={"name": "python"},
        )
    )

    payload = json.loads(response.content)

    assert payload["method"] == "PUT"
    assert payload["content_type"] == "application/json"
    assert json.loads(payload["body"]) == {"name": "python"}


async def test_send_timeout(server: TestServer, session: AiohttpSession) -> None:
    with pytest.raises(NetworkError):
        await session.send(
            Request(http_method=HTTPMethod.GET, url=str(server.make_url("/slow")))
        )


async def test_send_connection_error() -> None:
    session = AiohttpSession()

    try:
        with pytest.raises(NetworkError):
            await session.send(
                Request(http_method=HTTPMethod.GET, url="http://127.0.0.1:1/me")
            )
    finally:
        await session.close()


async def test_recreate_closed_session(session: AiohttpSession) -> None:
    first = await session.create_session()
    await session.close()

    second = await session.create_session()

    assert first.closed
    assert second is not first
    assert not second.closed
