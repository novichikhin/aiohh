from datetime import date

import pytest

from aiohh.client.session.base import Response
from aiohh.enums.host import Host
from aiohh.enums.http_method import HTTPMethod
from aiohh.exceptions.api import (
    APIError,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    ServerError,
    TooManyRequestsError,
    UnauthorizedError,
)
from aiohh.exceptions.decode import ClientDecodeError
from aiohh.methods.get_application_token import GetApplicationToken
from aiohh.methods.get_area import GetArea
from aiohh.methods.get_vacancy import GetVacancy
from aiohh.methods.invalidate_token import InvalidateToken
from aiohh.methods.search_vacancies import SearchVacancies
from aiohh.types.vacancy import Vacancy
from tests.conftest import FakeSession, load_fixture


def test_build_get_request(session: FakeSession) -> None:
    method = SearchVacancies(
        text="python",
        area=[1, "2"],
        clusters=True,
        no_magic=False,
        date_from=date(2026, 1, 1),
        host=Host.HH_KZ,
    )

    request = session.build_request(method=method, headers={"X": "1"})

    assert request.http_method is HTTPMethod.GET
    assert request.url == "https://api.hh.ru/vacancies"
    assert request.headers == {"X": "1"}
    assert request.params == [
        ("host", "hh.kz"),
        ("text", "python"),
        ("area", "1"),
        ("area", "2"),
        ("date_from", "2026-01-01"),
        ("clusters", "true"),
        ("no_magic", "false"),
    ]
    assert request.json is None
    assert request.data is None


def test_build_request_with_path_params(session: FakeSession) -> None:
    request = session.build_request(
        method=GetArea(area_id="1/2", locale="EN"), headers={}
    )

    assert request.url == "https://api.hh.ru/areas/1%2F2"
    assert request.params == [("locale", "EN")]


def test_build_form_request(session: FakeSession) -> None:
    method = GetApplicationToken(client_id="id", client_secret="secret", host="hh.ru")

    request = session.build_request(method=method, headers={})

    assert request.http_method is HTTPMethod.POST
    assert request.url == "https://api.hh.ru/token"
    assert request.params == [("host", "hh.ru")]
    assert request.data == [
        ("grant_type", "client_credentials"),
        ("client_id", "id"),
        ("client_secret", "secret"),
    ]
    assert request.json is None


def test_custom_api_url() -> None:
    session = FakeSession()
    session.api_url = "https://example.com"

    request = session.build_request(method=GetVacancy(vacancy_id=1), headers={})

    assert request.url == "https://example.com/vacancies/1"


def test_parse_response(session: FakeSession) -> None:
    response = Response(status_code=200, content=load_fixture("vacancy.json"))

    vacancy = session.parse_response(method=GetVacancy(vacancy_id=1), response=response)

    assert isinstance(vacancy, Vacancy)


def test_parse_empty_response(session: FakeSession) -> None:
    response = Response(status_code=204, content=b"")

    assert session.parse_response(method=InvalidateToken(), response=response) is None


@pytest.mark.parametrize("content", [b"", b"not json", b'{"id": 1}'])
def test_parse_invalid_response(session: FakeSession, content: bytes) -> None:
    response = Response(status_code=200, content=content)

    with pytest.raises(ClientDecodeError):
        session.parse_response(method=GetVacancy(vacancy_id=1), response=response)


@pytest.mark.parametrize(
    ("status_code", "error_class"),
    [
        (400, BadRequestError),
        (401, UnauthorizedError),
        (403, ForbiddenError),
        (404, NotFoundError),
        (409, ConflictError),
        (429, TooManyRequestsError),
        (500, ServerError),
        (503, ServerError),
        (418, APIError),
    ],
)
def test_parse_error_status(
    session: FakeSession, status_code: int, error_class: type[APIError]
) -> None:
    response = Response(status_code=status_code, content=b"")

    with pytest.raises(error_class) as error:
        session.parse_response(method=GetVacancy(vacancy_id=1), response=response)

    assert type(error.value) is error_class
    assert error.value.status_code == status_code
    assert error.value.errors == []


def test_parse_api_error(session: FakeSession) -> None:
    content = (
        b'{"errors": [{"type": "oauth", "value": "token_expired"}],'
        b' "description": "Forbidden", "oauth_error": "token-expired",'
        b' "request_id": "42"}'
    )
    method = GetVacancy(vacancy_id=1)

    with pytest.raises(ForbiddenError) as error:
        session.parse_response(
            method=method, response=Response(status_code=403, content=content)
        )

    assert error.value.method == method
    assert error.value.description == "Forbidden"
    assert error.value.request_id == "42"
    assert error.value.oauth_error == "token-expired"
    assert error.value.has_error("oauth", "token_expired")
    assert not error.value.has_error("oauth", "token_revoked")
    assert str(error.value) == (
        "GetVacancy failed with status 403: oauth=token_expired: Forbidden: "
        "request_id=42"
    )


def test_parse_captcha_error(session: FakeSession) -> None:
    content = (
        b'{"errors": [{"type": "captcha_required", "value": "captcha_required",'
        b' "captcha_url": "https://hh.ru/captcha"}], "request_id": "1"}'
    )

    with pytest.raises(ForbiddenError) as error:
        session.parse_response(
            method=GetVacancy(vacancy_id=1),
            response=Response(status_code=403, content=content),
        )

    assert error.value.captcha_url == "https://hh.ru/captcha"


def test_parse_oauth_error(session: FakeSession) -> None:
    content = b'{"error": "invalid_grant", "error_description": "code expired"}'

    with pytest.raises(BadRequestError) as error:
        session.parse_response(
            method=GetApplicationToken(client_id="id", client_secret="secret"),
            response=Response(status_code=400, content=content),
        )

    assert error.value.has_error("invalid_grant", "code expired")
