from datetime import UTC, datetime, timedelta

from core.archive.case_manager import CaseManager
from core.briefings.mission_brief import MissionBrief
from core.events.council_event import CouncilEvent
from core.events.event import Event
from core.models.observation import Observation
from core.models.relationship import Relationship
from core.models.tool_run import ToolRun
from core.services.id_generator import IdGenerator
from core.services.tool_run_service import ToolRunService


def assert_utc_aware(value: datetime) -> None:
    assert value.tzinfo is not None
    assert value.utcoffset() == timedelta(0)


def test_timestamp_defaults_are_timezone_aware():
    observation = Observation(
        id="OBS-2026-0001",
        mission_id=None,
        tool_run_id=None,
        evidence_id=None,
        category="system",
        data={},
    )

    relationship = Relationship(
        id="REL-2026-0001",
        source_id="ENT-2026-0001",
        target_id="ENT-2026-0002",
        relationship_type="observed-with",
    )

    tool_run = ToolRun(
        id="RUN-2026-0001",
        tool="test",
        target="localhost",
    )

    brief = MissionBrief(
        mission_id=None,
        target="localhost",
        executive_summary="Timestamp test.",
        confidence=1.0,
    )

    council_event = CouncilEvent(
        actor="Medusa",
        message="Timestamp test.",
    )

    event = Event(
        event_type="TimestampTest",
        payload={},
    )

    timestamps = (
        observation.observed_at,
        relationship.created_at,
        tool_run.started,
        tool_run.finished,
        brief.generated_at,
        council_event.created_at,
        event.timestamp,
    )

    for timestamp in timestamps:
        assert_utc_aware(timestamp)


def test_services_generate_timezone_aware_records():
    run = ToolRunService().create(
        tool="test",
        target="localhost",
    )

    assert_utc_aware(run.started)
    assert_utc_aware(run.finished)

    current_year = datetime.now(UTC).year
    observation_id = IdGenerator.next("OBS")

    assert observation_id.startswith(
        f"OBS-{current_year}-"
    )


def test_case_manager_serializes_utc_offset():
    mission = CaseManager().create_case(
        target="localhost",
        run_id="RUN-2026-0001",
    )

    created_at = datetime.fromisoformat(
        mission["created"]
    )

    assert_utc_aware(created_at)
    assert mission["created"].endswith("+00:00")
