from abc import ABC
from types import TracebackType
from typing import Optional, Type

from aiohh.methods.base import BaseMethod, ReturningType

HH_OAUTH_TOKEN_HEADER_KEY = "OauthToken"
HH_OAUTH_TOKEN_HEADER_VALUE = "Bearer {oauth_token}"

HH_USER_AGENT_HEADER_KEY = "HH-User-Agent"
HH_USER_AGENT_HEADER_VALUE = "aiohh/{version} ({email})"


class BaseAPI(ABC):

    async def __aenter__(self) -> "BaseAPI":
        raise NotImplementedError

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        raise NotImplementedError

    async def __call__(
        self,
        method: BaseMethod[ReturningType]
    ) -> ReturningType:
        raise NotImplementedError
