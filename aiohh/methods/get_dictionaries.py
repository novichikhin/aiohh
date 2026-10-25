from aiohh.methods.base import BaseMethod
from aiohh.types.dictionaries import Dictionaries


class GetDictionaries(BaseMethod[Dictionaries]):
    __returning__ = Dictionaries
    __endpoint__ = "/dictionaries"
