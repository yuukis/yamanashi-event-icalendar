import requests
import datetime
from dateutil.relativedelta import relativedelta


class ConpassEventRequest:

    def __init__(self, prefecture="", keyword=None, series_ids=None,
                 months=None):
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

        page_size = 100
        params["count"] = page_size
        params["order"] = 2
        page = 0
        events = []
        while True:
            params["start"] = page * page_size + 1
            response = self.__get(params)
            json = response.json()
            events += json['events']

            if json['results_returned'] < page_size:
                break
            page += 1

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
        return event["address"].startswith(self.prefecture)
