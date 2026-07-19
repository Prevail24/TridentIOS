import re
from urllib.parse import urljoin

from core.models.web_path_observation import WebPathObservation
from core.models.web_vhost_observation import WebVhostObservation


class GobusterParser:
    """
    Parses Gobuster directory-mode output into tool-neutral
    WebPathObservation objects.

    Supported examples:

        assets       (Status: 301) [Size: 178]
        assets       (Status: 301) [Size: 178] [--> http://host/assets/]
        index.php    (Status: 200) [Size: 12272]
    """
    ANSI_PATTERN = re.compile(
        r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])"
    )
    
    LINE_PATTERN = re.compile(
        r"^(?P<path>\S+)"
        r"\s+\(Status:\s*(?P<status>\d{3})\)"
        r"(?:\s+\[Size:\s*(?P<size>\d+)\])?"
        r"(?:\s+\[-->\s*(?P<redirect>[^\]]+)\])?"
        r"\s*$"
    )
    VHOST_LINE_PATTERN = re.compile(
        r"^(?P<hostname>\S+)"
        r"\s+Status:\s*(?P<status>\d{3})"
        r"(?:\s+\[Size:\s*(?P<size>\d+)\])?"
        r"(?:\s+\[-->\s*(?P<redirect>[^\]]+)\])?"
        r"\s*$"
    )

    def parse(
        self,
        raw_output: str,
        *,
        base_url: str,
    ) -> list[WebPathObservation]:
        observations = []

        normalized_base_url = base_url.rstrip("/") + "/"

        for line_number, raw_line in enumerate(
            raw_output.splitlines(),
            start=1,
        ):
            line = self.ANSI_PATTERN.sub("", raw_line).strip()

            if not line:
                continue

            match = self.LINE_PATTERN.match(line)

            if match is None:
                raise ValueError(
                    "Unable to parse Gobuster output "
                    f"at line {line_number}: {raw_line!r}"
                )

            path = match.group("path")
            status_code = int(match.group("status"))

            size_text = match.group("size")
            content_length = (
                int(size_text)
                if size_text is not None
                else None
            )

            redirect_location = match.group("redirect")

            observations.append(
                WebPathObservation(
                    base_url=base_url.rstrip("/"),
                    path=path,
                    url=urljoin(
                        normalized_base_url,
                        path.lstrip("/"),
                    ),
                    status_code=status_code,
                    content_length=content_length,
                    redirect_location=redirect_location,
                )
            )

        return observations

    def parse_vhosts(
        self,
        raw_output: str,
        *,
        base_url: str,
    ) -> list[WebVhostObservation]:
        observations = []
        scheme = base_url.split("://", 1)[0] if "://" in base_url else "http"

        for line_number, raw_line in enumerate(
            raw_output.splitlines(),
            start=1,
        ):
            line = self.ANSI_PATTERN.sub("", raw_line).strip()

            if not line:
                continue

            match = self.VHOST_LINE_PATTERN.match(line)

            if match is None:
                raise ValueError(
                    "Unable to parse Gobuster vhost output "
                    f"at line {line_number}: {raw_line!r}"
                )

            hostname = match.group("hostname")
            status_code = int(match.group("status"))

            size_text = match.group("size")
            content_length = (
                int(size_text)
                if size_text is not None
                else None
            )

            redirect_location = match.group("redirect")

            observations.append(
                WebVhostObservation(
                    base_url=base_url.rstrip("/"),
                    hostname=hostname,
                    url=f"{scheme}://{hostname}",
                    status_code=status_code,
                    content_length=content_length,
                    redirect_location=redirect_location,
                )
            )

        return observations
