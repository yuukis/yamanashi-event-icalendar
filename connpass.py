import requests
import datetime
from dateutil.relativedelta import relativedelta
from enum import Enum


class ConpassEventOrder(Enum):
    UPDATE = 1
    START = 2
    NEW = 3


class ConpassEventRequest:
    def __init__(self,
                 prefecture="",
                 keyword=None,
                 series_ids=None,
                 months=None,
                 count=100,
                 order=ConpassEventOrder.NEW):
        self.url = "https://connpass.com/api/v1/event/"
        self.prefecture = prefecture
        if keyword is None:
            self.keyword = []
        else:
            self.keyword = keyword
        if series_ids is None:
            self.series_ids = []
        else:
            self.series_ids = series_ids
        self.months = months
        self.count = count
        self.order = order

    def get_events(self):
        params = {}
        if self.prefecture != "":
            self.keyword.append(self.prefecture)
        if len(self.keyword) > 0:
            params["keyword"] = ",".join(self.keyword)
        if len(self.series_ids) > 0:
            params["series_id"] = ",".join(self.series_ids)
        if self.months is not None:
            delta = self.months
            month_array = []
            now = datetime.datetime.now()
            for i in range(-delta, delta + 1):
                month = now + relativedelta(months=i)
                month_array.append(month.strftime("%Y%m"))
            ym = ",".join(month_array)
            params["ym"] = ym

        if self.count is not None:
            params["count"] = self.count
        if self.order is not None:
            params["order"] = self.order.value

        response = self.__get(params)
        events = response.json()['events']

        if self.prefecture != "":
            events = list(filter(self.__is_in_pref, events))

        return events

    def __get(self, params):
        headers = {
            "User-Agent": "EventCalendarBot/1.0"
        }
        response = requests.get(self.url, headers=headers, params=params)
        return response

    def __is_in_pref(self, event):
        if event["address"] is None:
            return False
        return event["address"].startswith(self.prefecture)
