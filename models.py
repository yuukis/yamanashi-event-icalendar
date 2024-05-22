from typing import Optional
from dataclasses import dataclass


@dataclass
class Event:
    event_id: int
    title: str
    event_url: str
    started_at: str
    ended_at: str
    updated_at: str
    place: Optional[str]
    address: Optional[str]

    @staticmethod
    def from_json(json: dict):
        events = []

        for item in json:
            events.append(
                Event(
                    event_id=item["event_id"],
                    title=item["title"],
                    event_url=item["event_url"],
                    started_at=item["started_at"],
                    ended_at=item["ended_at"],
                    updated_at=item["updated_at"],
                    place=item["place"],
                    address=item["address"],
                )
            )
        return events
