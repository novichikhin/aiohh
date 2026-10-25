from aiohh.methods.base import BaseMethod
from aiohh.types.employer import AvailablePublications


class GetAvailablePublications(BaseMethod[AvailablePublications]):
    __returning__ = AvailablePublications
    __endpoint__ = "/employers/{employer_id}/services/available_publications"

    employer_id: int | str
    area_id: int | str | None = None
    professional_role_id: int | str | None = None
