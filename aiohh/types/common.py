from typing import Generic, TypeVar

from pydantic import Field

from aiohh.types.base import BaseType

ItemType = TypeVar("ItemType")


class Id(BaseType):
    id: str


class IdName(BaseType):
    id: str
    name: str


class Link(BaseType):
    url: str


class AreaLink(BaseType):
    id: str
    name: str
    url: str


class LogoUrls(BaseType):
    size_90: str | None = Field(default=None, alias="90")
    size_240: str | None = Field(default=None, alias="240")
    original: str | None = None


class Items(BaseType, Generic[ItemType]):
    items: list[ItemType]


class Page(Items[ItemType], Generic[ItemType]):
    found: int
    page: int
    pages: int
    per_page: int
