from core.engine import TridentEngine
from core.rendering.terminal_renderer import TerminalRenderer
from core.services.active_mission_service import ActiveMissionService


def new_mission() -> None:
    renderer = TerminalRenderer()
    renderer.banner("Mission Control")

    title = input("Mission Name   : ").strip()
    mission_type = input("Mission Type   : ").strip()
    objective = input("Objective      : ").strip()
    scope = input("Scope          : ").strip()
    operator = input("Operator       : ").strip() or "Prevail"
    priority = input("Priority       : ").strip() or "normal"

    engine = TridentEngine()

    result = engine.missions.create(
        title=title,
        mission_type=mission_type,
        objective=objective,
        scope=scope,
        operator=operator,
        priority=priority,
    )

    renderer.success(
        "⚓ Mission Established",
        f"""Mission ID

{result.mission.id}

Status

{result.mission.status.upper()}

Workspace

missions/{result.mission.id}/

Saved To

{result.filepath}

Recommended Playbook

TRD-PB-001 Quick Recon""",
    )


def start_mission(name: str) -> None:
    renderer = TerminalRenderer()
    engine = TridentEngine()
    active = ActiveMissionService()

    result = engine.missions.create(
        title=name,
        mission_type="investigation",
        objective="Active Trident mission",
        scope="unspecified",
        operator="Prevail",
        priority="normal",
    )

    active.activate(result.mission.id)

    renderer.success(
        "🔱 Mission Activated",
        f"""Mission ID

{result.mission.id}

Name

{result.mission.title}

Status

{result.mission.status.upper()}

Workspace

missions/{result.mission.id}/""",
    )


def mission_status() -> None:
    renderer = TerminalRenderer()
    active = ActiveMissionService()

    mission_id = active.current()

    if mission_id is None:
        renderer.warning("No Active Mission", "Start one with: trident mission start <name>")
        return

    renderer.success(
        "🔱 Active Mission",
        f"""Mission ID

{mission_id}""",
    )


def stop_mission() -> None:
    renderer = TerminalRenderer()
    active = ActiveMissionService()

    mission_id = active.current()

    if mission_id is None:
        renderer.warning("No Active Mission", "There is no active mission to stop.")
        return

    active.clear()

    renderer.success(
        "Mission Closed",
        f"""Closed Mission

{mission_id}""",
    )