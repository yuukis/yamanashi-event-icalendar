import os
import datetime
from dotenv import load_dotenv
from request import YamanashiEventRequest
from ical import ICalendarWriter
from github import GitHubUploader

load_dotenv()


def main(ics_file="event.ics"):
    now = datetime.datetime.now()
    from_year = now.year - 2
    from_month = now.month
    to_year = now.year + 1
    to_month = now.month
    events = YamanashiEventRequest(from_year, from_month, to_year,
                                   to_month).get_events()

    calendar_name = "IT勉強会 - 山梨県"
    calendar_description = "山梨県で開催されるIT勉強会イベントカレンダー"
    ICalendarWriter(
        events,
        name=calendar_name,
        description=calendar_description
    ).write(ics_file)

    GitHubUploader(
        token=os.getenv("GITHUB_TOKEN"),
        owner=os.getenv("GITHUB_OWNER"),
        repo=os.getenv("GITHUB_REPO")
    ).upload(ics_file)


if __name__ == "__main__":
    main()
