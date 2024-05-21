import requests
from models import Event


class YamanashiEventRequest:

    def __init__(self, from_year, from_month, to_year, to_month):
        host = "https://api.event.yamanashi.dev"
        path = f"/events/from/{from_year}/{from_month}/to/{to_year}/{to_month}"
        self.url = host + path

    def get_events(self):
        params = {}
        response = self.__get(params)

        json = response.json()
        events = Event.from_json(json)

        return events

    def __get(self, params):
        url = self.url

        print({"url": url})
        response = requests.get(url)

        return response
