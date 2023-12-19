from connpass import ConpassEventRequest
from ical import ICalendarWriter

# 山梨県で開催されたIT勉強会コミュニティ
SERIES_IDS = [
    "1678",   # 日本Androidの会 山梨支部
    "4255",   # 子ども向けプログラミングクラブ コーダー道場甲府
    "5327",   # Redmineプラグインもくもく会 山梨
    "7069",   # shingen.py
    "7465",   # 子どものためのプログラミングクラブ CoderDojo北杜
    "7466",   # 子どものためのプログラミングクラブ CoderDojo韮崎
    "7759",   # 山梨IT同好会(仮)
    "9176",   # 富士もくもく会
    "10940",  # 山梨Web勉強会
    "11367"   # 山梨SPA
]


def distinct_by_key(data: list[dict], key: str) -> list[dict]:
    return list({element[key]: element for element in data}.values())


def main(ics_file="event.ics"):
    events1 = ConpassEventRequest(prefecture="山梨県", months=6).get_events()
    events2 = ConpassEventRequest(series_ids=SERIES_IDS, months=6).get_events()
    events = distinct_by_key(events1 + events2, "event_id")
    events.sort(key=lambda x: x["started_at"])

    calendar_name = "IT勉強会 - 山梨県"
    calendar_description = "山梨県で開催されるIT勉強会イベントカレンダー"
    ICalendarWriter(
        events,
        name=calendar_name,
        description=calendar_description
    ).write(ics_file)


if __name__ == "__main__":
    main()
