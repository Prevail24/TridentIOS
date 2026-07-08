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