from core.events.event_bus import event_bus
from core.serpents.sentinel import Sentinel
from core.services.observation_service import ObservationService


sentinel = Sentinel()

event_bus.subscribe(
    "ObservationCreated",
    sentinel.handle,
)

service = ObservationService()


print()
print("SENTINEL")
print("--------")

print()
print("FIRST OBSERVATION")

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
print("SECOND OBSERVATION")

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
print("THIRD OBSERVATION")

service.create(
    category="http",
    data={
        "host": "45.33.32.156",
        "port": 80,
        "server": "nginx",
        "status": 200,
    },
)