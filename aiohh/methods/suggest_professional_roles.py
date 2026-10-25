from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.suggests import ProfessionalRoleSuggest


class SuggestProfessionalRoles(BaseMethod[Items[ProfessionalRoleSuggest]]):
    __returning__ = Items[ProfessionalRoleSuggest]
    __endpoint__ = "/suggests/professional_roles"

    text: str
