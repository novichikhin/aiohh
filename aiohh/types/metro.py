from aiohh.types.base import BaseType


class MetroLineInfo(BaseType):
    id: str
    name: str
    hex_color: str


class MetroStation(BaseType):
    id: str
    name: str
    lat: float | None = None
    lng: float | None = None
    order: int
    line: MetroLineInfo


class MetroLine(MetroLineInfo):
    stations: list[MetroStation] = []


class MetroCity(BaseType):
    id: str
    name: str
    url: str | None = None
    lines: list[MetroLine] = []
