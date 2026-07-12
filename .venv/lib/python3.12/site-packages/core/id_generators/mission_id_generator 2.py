from core.id_generators.id_generator import IDGenerator


class MissionIDGenerator(IDGenerator):
    """
    Generates Mission IDs.

    Example:
        MIS-2026-0001
    """

    def __init__(self):
        super().__init__("MIS")