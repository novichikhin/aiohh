from aiohh.methods.base import BaseMethod
from aiohh.types.dictionaries import ProfessionalRolesCatalog


class GetProfessionalRoles(BaseMethod[ProfessionalRolesCatalog]):
    __returning__ = ProfessionalRolesCatalog
    __endpoint__ = "/professional_roles"
