from core.events.event_bus import EventBus
from core.serpents.hunter import Hunter
from core.serpents.sentinel import Sentinel
from core.services.observation_service import ObservationService


bus = EventBus()
sentinel = Sentinel(bus=bus)
hunter = Hunter(bus=bus)
service = ObservationService(bus=bus)

received_recommendations = []


def receive_recommendation(event):
    received_recommendations.append(event)

    print()
    print("INVESTIGATION RECOMMENDED")
    print("-------------------------")
    print("Category:", event.payload["category"])
    print("Reason:", event.payload["reason"])

    for recommendation in event.payload["recommendations"]:
        print("-", recommendation)


bus.subscribe("ObservationCreated", sentinel.handle)
bus.subscribe("InfrastructureChanged", hunter.handle)
bus.subscribe("InvestigationRecommended", receive_recommendation)


print()
print("FIRST OBSERVATION")
print("-----------------")

service.create(
    category="http",
    data={
        "host": "45.33.32.156",
        "port": 80,
        "server": "Apache",
        "status": 200,
    },
)


print()
print("UNCHANGED OBSERVATION")
print("---------------------")

service.create(
    category="http",
    data={
        "host": "45.33.32.156",
        "port": 80,
        "server": "Apache",
        "status": 200,
    },
)


print()
print("CHANGED OBSERVATION")
print("-------------------")

service.create(
    category="http",
    data={
        "host": "45.33.32.156",
        "port": 80,
        "server": "nginx",
        "status": 200,
    },
)


assert len(received_recommendations) == 1

event = received_recommendations[0]

assert event.event_type == "InvestigationRecommended"
assert event.payload["category"] == "http"
assert event.payload["previous"]["server"] == "Apache"
assert event.payload["current"]["server"] == "nginx"

print()
print("Hunter followed Sentinel's signal.")