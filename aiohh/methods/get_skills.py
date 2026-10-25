from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.dictionaries import Skill


class GetSkills(BaseMethod[Items[Skill]]):
    __returning__ = Items[Skill]
    __endpoint__ = "/skills"

    id: list[int | str]
