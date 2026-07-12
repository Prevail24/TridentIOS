from core.repositories.observation_repository import ObservationRepository
from core.repositories.tool_run_repository import ToolRunRepository


class ToolRunSnapshotService:
    """
    Builds an immutable intelligence snapshot from one ToolRun.

    A snapshot is derived only from observations owned by that run.
    It does not read the accumulated Loom state.
    """

    def __init__(self):
        self.tool_runs = ToolRunRepository()
        self.observations = ObservationRepository()

    def build(self, run_id: str) -> dict:
        run = self.tool_runs.open(run_id)

        snapshot = {
            "run_id": run.id,
            "tool": run.tool,
            "target": run.target,
            "mission_id": run.mission_id,
            "started": run.started,
            "finished": run.finished,
            "ports": [],
            "services": [],
            "products": [],
            "versions": [],
            "urls": [],
            "status_codes": [],
            "web_servers": [],
            "technologies": [],
            "ip_addresses": [],
        }

        for observation_id in run.observations:
            observation = self.observations.open(observation_id)
            data = observation.data

            if observation.category == "port":
                protocol = data.get("protocol")
                port = data.get("port")

                if protocol and port is not None:
                    snapshot["ports"].append(f"{protocol}/{port}")

                self._append(snapshot["services"], data.get("service"))
                self._append(snapshot["products"], data.get("product"))
                self._append(snapshot["versions"], data.get("version"))

            elif observation.category == "http_endpoint":
                scheme = data.get("scheme")
                port = data.get("port")

                if scheme and port is not None:
                    snapshot["ports"].append(f"{scheme}/{port}")

                self._append(snapshot["urls"], data.get("url"))
                self._append(snapshot["status_codes"], data.get("status_code"))
                self._append(snapshot["web_servers"], data.get("webserver"))
                self._append(snapshot["ip_addresses"], data.get("host_ip"))

                for technology in data.get("technologies", []):
                    self._append(snapshot["technologies"], technology)

                for address in data.get("ipv4_addresses", []):
                    self._append(snapshot["ip_addresses"], address)

                for address in data.get("ipv6_addresses", []):
                    self._append(snapshot["ip_addresses"], address)

        for field, value in snapshot.items():
            if isinstance(value, list):
                snapshot[field] = sorted(set(value), key=str)

        return snapshot

    @staticmethod
    def _append(collection: list, value) -> None:
        if value is not None and value != "":
            collection.append(value)