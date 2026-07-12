from core.engine import TridentEngine
from core.rendering.terminal_renderer import TerminalRenderer


def create_evidence():
    renderer = TerminalRenderer()
    renderer.banner("Collect Evidence")

    title = input("Evidence Title : ")
    evidence_type = input("Type           : ")
    source = input("Source         : ")
    observation_id = input("Observation ID : ")

    engine = TridentEngine()

    result = engine.evidence.create(
        title=title,
        evidence_type=evidence_type,
        source=source,
        observation_id=observation_id,
    )

    renderer.success(
        "✓ Evidence Collected",
        f"""Evidence ID

    {result.evidence.id}

    Attached To

    {result.evidence.observation_id}
    """,
    )