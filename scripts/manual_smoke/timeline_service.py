from core.services.timeline_service import TimelineService


service = TimelineService()

timeline = service.build("45.33.32.156")

print()
print("HOST TIMELINE")
print("-------------")

for event in timeline:
    data = event["data"]

    print(
        f"{event['observed_at']} | "
        f"{event['category']} | "
        f"{data.get('protocol')}/{data.get('port')} | "
        f"{data.get('service')}"
    )