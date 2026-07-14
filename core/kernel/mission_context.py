from core.models.tool_run import ToolRun
from core.repositories.tool_run_repository import ToolRunRepository
from core.services.state_service import StateService
from core.models.observation import Observation
from core.repositories.observation_repository import ObservationRepository

class MissionContext:
    """
    Provides live operational awareness for the active mission.

    Observer, Council members, dashboards, and future advisors
    should query this object instead of reading runtime files directly.
    """

    def __init__(self):
        self.state = StateService()
        self.tool_runs = ToolRunRepository()
        self.observations = ObservationRepository()

    def mission_observations(self) -> list[Observation]:
        """
        Return every canonical observation belonging to the active mission.
        """
        mission_id = self.require_mission_id()

        return [
            observation
            for observation in self.observations.list()
            if observation.mission_id == mission_id
        ]


    def open_ports(self) -> list[dict]:
        """
        Return normalized open-port intelligence for the active mission.
        """
        ports = []

        for observation in self.mission_observations():
            if observation.category != "port":
                continue

            data = observation.data or {}
            state = str(data.get("state", "")).lower()

            if state and state != "open":
                continue

            try:
                port = int(data.get("port"))
            except (TypeError, ValueError):
                continue

            ports.append(
                {
                    "host": data.get("host", "Unknown"),
                    "port": port,
                    "protocol": data.get("protocol", "tcp"),
                    "service": data.get("service", "unknown"),
                    "product": data.get("product", ""),
                    "version": data.get("version", ""),
                    "extrainfo": data.get("extrainfo", ""),
                    "observation_id": observation.id,
                }
            )

        return sorted(
            ports,
            key=lambda item: (
                str(item["host"]),
                item["port"],
                str(item["protocol"]),
            ),
        )

    def current_mission_id(self) -> str | None:
        return self.state.get_active_mission()

    def require_mission_id(self) -> str:
        mission_id = self.current_mission_id()

        if mission_id is None:
            raise RuntimeError(
                "No active mission. Start or activate a mission first."
            )

        return mission_id

    def runs(self) -> list[ToolRun]:
        mission_id = self.require_mission_id()

        return [
            run
            for run in self.tool_runs.list()
            if run.mission_id == mission_id
        ]

    def enrich(self, payload: dict) -> dict:
        return {
            "mission_id": self.current_mission_id(),
            **payload,
        }