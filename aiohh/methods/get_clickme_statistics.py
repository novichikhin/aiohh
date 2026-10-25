from datetime import date

from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.statistics import ClickmeStatisticsItem


class GetClickmeStatistics(BaseMethod[Items[ClickmeStatisticsItem]]):
    __returning__ = Items[ClickmeStatisticsItem]
    __endpoint__ = "/clickme/statistics"

    date_from: date
    date_to: date
    with_banners: bool | None = None
