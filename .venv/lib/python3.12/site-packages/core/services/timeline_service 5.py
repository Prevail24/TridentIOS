from core.repositories.observation_repository import ObservationRepository


class TimelineService:
    """
    Builds a chronological timeline for an asset.
    """

    def __init__(self):
        self.observations = ObservationRepository()

    def build(self, host: str):
        events = []

        for observation in self.observations.list():
            if observation.data.get("host") != host:
                continue

            events.append({
                "observed_at": observation.observed_at,
                "category": observation.category,
                "data": observation.data,
            })

        return sorted(events, key=lambda event: event["observed_at"])