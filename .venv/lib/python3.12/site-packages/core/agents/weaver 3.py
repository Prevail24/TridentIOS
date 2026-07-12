from dataclasses import dataclass


@dataclass
class WeaverReport:
    object_id: str
    object_type: str

    evidence_count: int = 0
    relationship_count: int = 0
    note_count: int = 0

    summary: str = ""


class Weaver:
    """
    The Weaver traverses The Loom.

    It discovers structure.

    It does not use AI.

    It reports facts.
    """

    def analyze_observation(self, observation):

        report = WeaverReport(
            object_id=observation.id,
            object_type="Observation",
            evidence_count=len(observation.evidence),
            note_count=len(observation.notes),
        )

        report.summary = (
            f"{observation.id} contains "
            f"{report.evidence_count} evidence item(s) "
            f"and {report.note_count} note(s)."
        )

        return report