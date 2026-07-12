from collections import defaultdict


class EventBus:
    """
    Simple publish / subscribe event bus.
    """

    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_type, handler):
        self._subscribers[event_type].append(handler)

    def publish(self, event):

        handlers = self._subscribers.get(event.event_type, [])

        for handler in handlers:
            handler(event)


from collections import defaultdict
from collections.abc import Callable

from core.events.event import Event


class EventBus:
    """
    Synchronous in-process event bus for Trident IOS.
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[Event], None]]] = defaultdict(list)

    def subscribe(
        self,
        event_type: str,
        handler: Callable[[Event], None],
    ) -> None:
        if handler not in self._subscribers[event_type]:
            self._subscribers[event_type].append(handler)

    def unsubscribe(
        self,
        event_type: str,
        handler: Callable[[Event], None],
    ) -> None:
        handlers = self._subscribers.get(event_type, [])

        if handler in handlers:
            handlers.remove(handler)

    def publish(self, event: Event) -> None:
        handlers = list(self._subscribers.get(event.event_type, []))

        for handler in handlers:
            handler(event)


# Shared nervous system for the running Trident process.
event_bus = EventBus()