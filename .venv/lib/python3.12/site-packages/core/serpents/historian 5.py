from core.services.chronicle_service import ChronicleService


class Historian:
    """
    Keeper of Time.

    Reconstructs investigations from canonical history.
    """

    def __init__(self):
        self.chronicle = ChronicleService()

    def reconstruct(self, host: str):
        return self.chronicle.build(host)