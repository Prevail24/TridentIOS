from urllib.parse import urlparse

from core.armory.httpx.sensor import HttpxSensor
from core.kernel.mission_context import MissionContext
from core.weapons import Weapon


class HttpxWeapon(Weapon):
    """
    Fingerprint the active mission's HTTP surface through HTTPX.
    """

    name = "HTTPX"
    description = "HTTP technology and endpoint discovery."

    def execute(self, context: MissionContext) -> dict:
        self.awaken()

        results = []

        for target in self._targets(context):
            result = HttpxSensor(target).collect()
            results.append(result)

            for host_header in self._redirect_hostnames(
                target,
                result["observations"],
            ):
                results.append(
                    HttpxSensor(
                        target,
                        host_header=host_header,
                    ).collect()
                )

        if len(results) == 1:
            return results[0]

        observations = []
        processed = []

        for result in results:
            observations.extend(result["observations"])
            processed.extend(result["processed"])

        return {
            "tool_run": results[0]["tool_run"],
            "tool_runs": [
                result["tool_run"]
                for result in results
            ],
            "observations": observations,
            "processed": processed,
        }

    def _targets(self, context: MissionContext) -> list[str]:
        ports = [
            port
            for port in context.open_ports()
            if self._is_http_port(port)
        ]

        if not ports:
            return [context.target()]

        targets = []

        for port in ports:
            scheme = "https" if port["port"] in {443, 8443} else "http"
            host = port["host"]
            number = port["port"]

            if (scheme, number) in {("http", 80), ("https", 443)}:
                targets.append(f"{scheme}://{host}")
            else:
                targets.append(f"{scheme}://{host}:{number}")

        return list(dict.fromkeys(targets))

    def _is_http_port(self, port: dict) -> bool:
        service = str(port.get("service") or "").lower()

        return (
            port.get("port") in {80, 443, 8000, 8008, 8080, 8081, 8443}
            or "http" in service
        )

    def _redirect_hostnames(
        self,
        target: str,
        observations: list,
    ) -> list[str]:
        target_host = urlparse(target).hostname
        hostnames = []

        for observation in observations:
            location = observation.data.get("redirect_location")

            if not location:
                continue

            redirect_host = urlparse(location).hostname

            if not redirect_host:
                continue

            if redirect_host == target_host:
                continue

            hostnames.append(redirect_host)

        return list(dict.fromkeys(hostnames))
