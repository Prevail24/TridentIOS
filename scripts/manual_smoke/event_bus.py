from core.events.event import Event
from core.events.event_bus import EventBus


bus = EventBus()


def observation_handler(event):

    print()

    print("EVENT RECEIVED")

    print("----------------")

    print(event.event_type)

    print(event.payload)


bus.subscribe(
    "ObservationCreated",
    observation_handler,
)

bus.publish(
    Event(
        event_type="ObservationCreated",
        payload={
            "host": "45.33.32.156",
            "sensor": "nmap",
        },
    )
)