import base64
import hashlib
from urllib.parse import parse_qs, urlsplit

from aiohh.utils.oauth import (
    build_authorization_url,
    create_code_challenge,
    generate_code_verifier,
)


def test_build_minimal_authorization_url() -> None:
    assert (
        build_authorization_url("client")
        == "https://hh.ru/oauth/authorize?response_type=code&client_id=client"
    )


def test_build_authorization_url() -> None:
    url = build_authorization_url(
        "client",
        redirect_uri="https://example.com/oauth?lang=RU",
        state="state",
        code_challenge="challenge",
        role="employer",
        force_role=True,
        skip_choose_account=False,
    )

    assert parse_qs(urlsplit(url).query) == {
        "response_type": ["code"],
        "client_id": ["client"],
        "redirect_uri": ["https://example.com/oauth?lang=RU"],
        "state": ["state"],
        "code_challenge": ["challenge"],
        "code_challenge_method": ["S256"],
        "role": ["employer"],
        "force_role": ["true"],
        "skip_choose_account": ["false"],
    }


def test_pkce() -> None:
    verifier = generate_code_verifier()
    expected = (
        base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest())
        .rstrip(b"=")
        .decode()
    )

    assert 43 <= len(verifier) <= 128
    assert create_code_challenge(verifier) == expected
