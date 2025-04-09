import datetime
from icalendar import Calendar, Event


class ICalendarWriter:
    def __init__(self, events, name=None, description=None):
        self.events = events
        self.name = name
        self.description = description
        self.calendar = None
        self.__build()

    def write(self, file):
        ical = self.calendar.to_ical()
        with open(file, "wb") as f:
            f.write(ical)

    def __build(self):
        cal = Calendar()
        cal.add("method", "PUBLISH")
        cal.add("version", "2.0")
        cal.add("prodid", "-//yuukis//yamanashi-icalendar-updater//JP")
        if self.name is not None:
            cal.add("x-wr-calname", self.name)
        if self.description is not None:
            cal.add("x-wr-caldesc", self.description)
        cal.add("x-wr-timezone", "Asia/Tokyo")

        for event in self.events:
            uid = f"connpass_{event.event_id}@calendar.yamanashi.dev"
            e = Event()
            e.add("uid", uid)
            e.add("summary", event.title)
            e.add("description", event.event_url)
            e.add("dtstart", self.__format_date(event.started_at))
            e.add("dtend", self.__format_date(event.ended_at))
            e.add("dtstamp", self.__format_date(event.updated_at))
            e.add("last-modified", self.__format_date(event.updated_at))
            if event.open_status == "cancelled":
                e.add("status", "CANCELLED")
            location_array = []
            if event.address is not None:
                location_array.append(event.address)
            if event.place is not None:
                location_array.append(event.place)
            location = " ".join(location_array)
            if location != "":
                e.add("location", location)
            cal.add_component(e)

        self.calendar = cal

    def __format_date(self, date):
        return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S+09:00")
