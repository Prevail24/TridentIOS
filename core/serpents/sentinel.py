from core.events.event import Event
from core.events.event_bus import EventBus, event_bus


class Sentinel:
    """
    Guardian of Change.

    Sentinel answers one question:

        "Did reality change?"

    When successive observations differ, Sentinel publishes
    an InfrastructureChanged event.
    """

    def __init__(self, bus: EventBus | None = None) -> None:
        self.bus = bus if bus is not None else event_bus
        self._latest: dict[str, dict] = {}

    def handle(self, event: Event) -> None:
        if event.event_type != "ObservationCreated":
            return

        category = event.payload["category"]
        current = event.payload["data"]
        previous = self._latest.get(category)

        if previous is None:
            print(f"👁 Sentinel: first {category} observation recorded.")

        elif previous == current:
            print("👁 Sentinel: no change.")

        else:
            print(f"👁 Sentinel: change detected in '{category}'.")

            self.bus.publish(
                Event(
                    event_type="InfrastructureChanged",
                    payload={
                        "category": category,
                        "previous": previous,
                        "current": current,
                        "observation_id": event.payload["observation_id"],
                        "mission_id": event.payload.get("mission_id"),
                        "tool_run_id": event.payload.get("tool_run_id"),
                        "detected_by": "Sentinel",
                    },
                )
            )

        self._latest[category] = current