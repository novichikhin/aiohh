from aiohh.methods.base import BaseMethod
from aiohh.types.manager import ManagerAccounts


class GetManagerAccounts(BaseMethod[ManagerAccounts]):
    __returning__ = ManagerAccounts
    __endpoint__ = "/manager_accounts/mine"
