from aiohh.types.base import BaseType


class Area(BaseType):
    id: str
    name: str
    parent_id: str | None = None
    lat: float | None = None
    lng: float | None = None
    utc_offset: str | None = None
    name_prepositional: str | None = None
    areas: list["Area"] = []
