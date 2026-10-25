from aiohh.methods.base import BaseMethod
from aiohh.types.employer_vacancy import PreferredNegotiationsOrder


class GetPreferredNegotiationsOrder(BaseMethod[PreferredNegotiationsOrder]):
    __returning__ = PreferredNegotiationsOrder
    __endpoint__ = "/vacancies/{vacancy_id}/preferred_negotiations_order"

    vacancy_id: int | str
