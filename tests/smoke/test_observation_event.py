from core.events.event_bus import event_bus
from core.services.observation_service import ObservationService


received_events = []


def receive_observation(event):
    received_events.append(event)

    print()
    print("OBSERVATION SIGNAL RECEIVED")
    print("---------------------------")
    print("Event:", event.event_type)
    print("Observation:", event.payload["observation_id"])
    print("Data:", event.payload["data"])
    print("Category:", event.payload["category"])


event_bus.subscribe(
    "ObservationCreated",
    receive_observation,
)

service = ObservationService()

result = service.create(
    category="system",
    data={
        "message": "Nervous System Test",
        "source": "trident",
    },
)

assert result.success is True
assert len(received_events) == 1
assert received_events[0].payload["observation_id"] == result.observation.id

print()
print("The Observatory felt its first pulse.")