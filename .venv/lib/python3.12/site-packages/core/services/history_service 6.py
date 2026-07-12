from core.repositories.observation_repository import ObservationRepository


class HistoryService:
    """
    Builds basic historical context for an asset.
    """

    def __init__(self):
        self.observations = ObservationRepository()

    def build(self, host: str):
        matching = []

        for observation in self.observations.list():
            if observation.data.get("host") == host:
                matching.append(observation)

        if not matching:
            return None

        timestamps = [
            observation.observed_at
            for observation in matching
            if observation.observed_at is not None
        ]

        return {
            "host": host,
            "observation_count": len(matching),
            "first_seen": min(timestamps) if timestamps else None,
            "last_seen": max(timestamps) if timestamps else None,
        }