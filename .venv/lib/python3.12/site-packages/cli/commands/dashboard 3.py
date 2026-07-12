from core.engine import TridentEngine
from core.rendering.terminal_renderer import TerminalRenderer


def show_dashboard():
    renderer = TerminalRenderer()
    renderer.banner("Observatory Dashboard")

    engine = TridentEngine()
    observations = engine.observations.list()

    renderer.success(
        "⚓ Trident Engine Online",
        f"""Observer

Prevail

Version

0.5.0-alpha

Threads

{len(observations)}

Status

The Loom is connected."""
    )

    renderer.archive(observations[-5:])