from core.services.timeline_service import TimelineService


def show_timeline(host: str):
    service = TimelineService()

    timeline = service.build(host)

    print()
    print("═══════════════════════════════")
    print("        HOST TIMELINE")
    print("═══════════════════════════════")
    print()

    for event in timeline:
        data = event["data"]

        print(
            f"{event['observed_at']} | "
            f"{event['category']} | "
            f"{data.get('protocol')}/{data.get('port')} | "
            f"{data.get('service')}"
        )