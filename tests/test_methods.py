import importlib
import inspect
import pkgutil
import re
from typing import Any

import pytest

import aiohh.methods
from aiohh.api.client import AiohhAPI
from aiohh.client.session.base import get_endpoint_fields, get_type_adapter
from aiohh.methods.add_chat_participant import AddChatParticipant
from aiohh.methods.add_employer_manager import AddEmployerManager
from aiohh.methods.base import BaseMethod
from aiohh.methods.get_chats import GetChats
from aiohh.methods.publish_vacancy import PublishVacancy
from aiohh.methods.send_chat_message import SendChatMessage
from aiohh.types.common import Id
from aiohh.types.manager import ManagerPhone
from aiohh.types.vacancy_input import (
    SalaryRangeInput,
    VacancyPropertiesInput,
    VacancyPropertyInput,
)
from tests.conftest import FakeSession


def collect_methods() -> list[type[BaseMethod[Any]]]:
    methods = []

    for module_info in pkgutil.iter_modules(aiohh.methods.__path__):
        module = importlib.import_module(f"aiohh.methods.{module_info.name}")

        for name, value in vars(module).items():
            if (
                inspect.isclass(value)
                and issubclass(value, BaseMethod)
                and value.__module__ == module.__name__
                and not name.startswith("Base")
            ):
                methods.append(value)

    return methods


METHODS = collect_methods()


def to_snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def field_names(method: type[BaseMethod[Any]]) -> set[str]:
    return {field.alias or name for name, field in method.model_fields.items()}


def test_methods_are_collected() -> None:
    assert len(METHODS) == 133


@pytest.mark.parametrize("method", METHODS, ids=lambda method: method.__name__)
def test_method_is_consistent(method: type[BaseMethod[Any]]) -> None:
    if method.__returning__ is not None:
        get_type_adapter(method.__returning__)

    assert get_endpoint_fields(method.__endpoint__) <= field_names(method)
    assert method.__query__ <= field_names(method)
    assert callable(getattr(AiohhAPI, to_snake_case(method.__name__), None))


def test_manager_account_header(session: FakeSession) -> None:
    api = AiohhAPI(
        user_agent="test",
        access_token="token",
        manager_account_id="42",
        session=session,
    )

    assert api.build_headers(AddChatParticipant(chat_id=1, manager_id=2)) == {
        "HH-User-Agent": "test",
        "Authorization": "Bearer token",
        "X-Manager-Account-Id": "42",
    }


def test_json_body_with_nested_models(session: FakeSession) -> None:
    method = PublishVacancy(
        name="Python developer",
        description="<p>Description</p>",
        area=Id(id="1"),
        vacancy_properties=VacancyPropertiesInput(
            properties=[VacancyPropertyInput(property_type="HH_STANDARD")]
        ),
        salary_range=SalaryRangeInput(
            currency="RUR", gross=False, from_=100000, mode=Id(id="MONTH")
        ),
        ignore_duplicates=True,
    )

    request = session.build_request(method=method, headers={})

    assert request.params == [("ignore_duplicates", "true")]
    assert request.json == {
        "name": "Python developer",
        "description": "<p>Description</p>",
        "area": {"id": "1"},
        "vacancy_properties": {"properties": [{"property_type": "HH_STANDARD"}]},
        "salary_range": {
            "currency": "RUR",
            "gross": False,
            "from": 100000,
            "mode": {"id": "MONTH"},
        },
    }


def test_default_body_value(session: FakeSession) -> None:
    method = AddEmployerManager(
        employer_id=1,
        email="manager@example.com",
        first_name="Ivan",
        last_name="Ivanov",
        position="HR",
        area=Id(id="1"),
        phone=ManagerPhone(country="7", city="999", number="1234567"),
        is_main_contact_person=False,
    )

    request = session.build_request(method=method, headers={})

    assert request.json["manager_type"] == {"id": "manager"}


def test_aliased_body_field(session: FakeSession) -> None:
    request = session.build_request(
        method=AddChatParticipant(chat_id=1, manager_id=2), headers={}
    )

    assert request.url == "https://api.hh.ru/common/chats/1/participants"
    assert request.json == {"id": 2}


def test_vacancy_ids_filter(session: FakeSession) -> None:
    request = session.build_request(
        method=GetChats(filter_with_vacancy_ids=[1, "2"], filter_unread=True),
        headers={},
    )

    assert request.params == [
        ("filter_unread", "true"),
        ("filter_with_vacancy_ids", "[1,2]"),
    ]


def test_idempotency_key() -> None:
    first = SendChatMessage(chat_id=1, text="Hi")
    second = SendChatMessage(chat_id=1, text="Hi")

    assert first.idempotency_key
    assert first.idempotency_key != second.idempotency_key
    assert SendChatMessage(chat_id=1, idempotency_key="key").idempotency_key == "key"
