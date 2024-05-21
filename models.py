from typing import Optional
from dataclasses import dataclass


@dataclass
class Event:
    event_id: int
    title: str
    catch: str
    hash_tag: str
    event_url: str
    started_at: str
    ended_at: str
    updated_at: str
    limit: Optional[int]
    accepted: Optional[int]
    waiting: Optional[int]
    owner_name: str
    place: Optional[str]
    address: Optional[str]
    group_name: Optional[str]
    group_url: Optional[str]

    @staticmethod
    def from_json(json: dict):
        events = []

        for item in json:
            events.append(
                Event(
                    event_id=item["event_id"],
                    title=item["title"],
                    catch=item["catch"],
                    hash_tag=item["hash_tag"],
                    event_url=item["event_url"],
                    started_at=item["started_at"],
                    ended_at=item["ended_at"],
                    updated_at=item["updated_at"],
                    limit=item["limit"],
                    accepted=item["accepted"],
                    waiting=item["waiting"],
                    owner_name=item["owner_name"],
                    place=item["place"],
                    address=item["address"],
                    group_name=item["group_name"],
                    group_url=item["group_url"]
                )
            )
        return events
