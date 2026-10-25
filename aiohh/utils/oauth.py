import base64
import hashlib
import secrets
from typing import Literal
from urllib.parse import urlencode

AUTHORIZATION_URL = "https://hh.ru/oauth/authorize"


def generate_code_verifier() -> str:
    return secrets.token_urlsafe(64)


def create_code_challenge(code_verifier: str) -> str:
    digest = hashlib.sha256(code_verifier.encode("ascii")).digest()

    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")


def build_authorization_url(
    client_id: str,
    *,
    redirect_uri: str | None = None,
    state: str | None = None,
    code_challenge: str | None = None,
    role: Literal["applicant", "employer"] | None = None,
    force_role: bool | None = None,
    force_login: bool | None = None,
    skip_choose_account: bool | None = None,
    authorization_url: str = AUTHORIZATION_URL,
) -> str:
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "state": state,
        "code_challenge": code_challenge,
        "code_challenge_method": code_challenge and "S256",
        "role": role,
        "force_role": force_role,
        "force_login": force_login,
        "skip_choose_account": skip_choose_account,
    }

    query = urlencode(
        {
            name: str(value).lower() if isinstance(value, bool) else value
            for name, value in params.items()
            if value is not None
        }
    )

    return f"{authorization_url}?{query}"
