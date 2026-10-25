import json
from datetime import datetime, timedelta, timezone

from aiohh.types.employer import Employer
from aiohh.types.vacancy import VacanciesPage, Vacancy
from tests.conftest import load_fixture


def test_vacancy() -> None:
    vacancy = Vacancy.model_validate_json(load_fixture("vacancy.json"))

    assert vacancy.id
    assert vacancy.published_at.tzinfo is not None
    assert vacancy.salary_range is not None
    assert vacancy.salary_range.from_ == 30000
    assert vacancy.model_extra is not None
    assert "salary" in vacancy.model_extra


def test_vacancies_page() -> None:
    page = VacanciesPage.model_validate_json(load_fixture("vacancies_page.json"))

    assert page.found > 0
    assert len(page.items) == 2
    assert page.items[0].employer is not None
    assert page.clusters


def test_employer() -> None:
    employer = Employer.model_validate_json(load_fixture("employer.json"))

    assert employer.name == "HeadHunter"
    assert employer.branding is not None
    assert employer.branding.makeup is not None


def test_datetime_with_offset_without_colon() -> None:
    payload = json.loads(load_fixture("vacancy.json"))
    payload["published_at"] = "2026-01-01T10:00:00+0300"

    vacancy = Vacancy.model_validate(payload)

    assert vacancy.published_at == datetime(
        2026, 1, 1, 10, tzinfo=timezone(timedelta(hours=3))
    )
