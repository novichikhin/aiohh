from aiohh.api.client import AiohhAPI
from aiohh.enums.host import Host
from aiohh.enums.http_method import HTTPMethod
from aiohh.types.vacancy import VacanciesPage, Vacancy
from tests.conftest import FakeSession, load_fixture


async def test_user_agent_header(api: AiohhAPI, session: FakeSession) -> None:
    session.add_response(load_fixture("vacancy.json"))

    await api.get_vacancy(1)

    assert session.requests[0].headers == {
        "HH-User-Agent": "aiohh-tests/1.0 (tests@example.com)"
    }


async def test_authorization_header(api: AiohhAPI, session: FakeSession) -> None:
    api.access_token = "token"
    session.add_response(load_fixture("vacancy.json"))

    await api.get_vacancy(1)

    assert session.requests[0].headers["Authorization"] == "Bearer token"


async def test_token_request_is_not_authorized(
    api: AiohhAPI, session: FakeSession
) -> None:
    api.access_token = "expired"
    session.add_response(
        {
            "access_token": "a",
            "refresh_token": "r",
            "expires_in": 1,
            "token_type": "bearer",
        }
    )

    token = await api.refresh_user_token("refresh")

    assert "Authorization" not in session.requests[0].headers
    assert session.requests[0].data == [
        ("grant_type", "refresh_token"),
        ("refresh_token", "refresh"),
    ]
    assert token.access_token == "a"


async def test_invalidate_token(api: AiohhAPI, session: FakeSession) -> None:
    api.access_token = "token"
    session.add_response(status_code=204)

    await api.invalidate_token()

    assert session.requests[0].http_method is HTTPMethod.DELETE
    assert session.requests[0].headers["Authorization"] == "Bearer token"


async def test_default_host_and_locale(session: FakeSession) -> None:
    api = AiohhAPI(user_agent="test", host=Host.HH_KZ, locale="EN", session=session)
    session.add_response(load_fixture("vacancy.json"))
    session.add_response(load_fixture("vacancy.json"))

    await api.get_vacancy(1)
    await api.get_vacancy(1, host=Host.RABOTA_BY)

    assert session.requests[0].params == [("host", "hh.kz"), ("locale", "EN")]
    assert session.requests[1].params == [("host", "rabota.by"), ("locale", "EN")]


async def test_search_vacancies(api: AiohhAPI, session: FakeSession) -> None:
    session.add_response(load_fixture("vacancies_page.json"))

    page = await api.search_vacancies(text="python", per_page=2)

    assert isinstance(page, VacanciesPage)
    assert len(page.items) == 2
    assert session.requests[0].url == "https://api.hh.ru/vacancies"
    assert session.requests[0].params == [("text", "python"), ("per_page", "2")]


async def test_get_vacancy(api: AiohhAPI, session: FakeSession) -> None:
    session.add_response(load_fixture("vacancy.json"))

    vacancy = await api.get_vacancy("123")

    assert isinstance(vacancy, Vacancy)
    assert session.requests[0].url == "https://api.hh.ru/vacancies/123"


async def test_context_manager_closes_session(session: FakeSession) -> None:
    async with AiohhAPI(user_agent="test", session=session):
        pass

    assert session.closed
