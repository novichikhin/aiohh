from dataclasses import dataclass
from typing import Optional, List

from pydantic import BaseModel

from aiohh.exceptions.base import AiohhError
from aiohh.methods.base import BaseMethod, ReturningType


class DetailedAPIError(BaseModel):
    type: str
    value: Optional[str] = None


@dataclass(frozen=True)
class APIError(AiohhError):
    method: BaseMethod[ReturningType]
    status_code: int
    detailed_errors: List[DetailedAPIError]
