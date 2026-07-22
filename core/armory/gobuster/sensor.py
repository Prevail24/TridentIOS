from core.armory.sensor import Sensor
from core.adapters.gobuster_adapter import GobusterAdapter
from core.parsers.gobuster.parser import GobusterParser


class GobusterSensor(Sensor):
    name = "gobuster"
    version = "0.1.0"

    produces = [
        "web_path",
        "url",
        "http_status",
        "content_length",
        "redirect_location",
    ]

    def __init__(
        self,
        target: str,
        wordlist: str,
        *,
        mode: str = "dir",
        host_header: str | None = None,
        extensions: str | None = None,
        domain: str | None = None,
        append_domain: bool = True,
        status_codes_blacklist: str = "302,404",
        exclude_status: str | None = None,
        threads: int = 10,
    ):
        self.target = target
        self.wordlist = wordlist
        self.mode = mode
        self.host_header = host_header
        self.extensions = extensions
        self.domain = domain
        self.append_domain = append_domain

        self.adapter = GobusterAdapter(
            target=target,
            wordlist=wordlist,
            mode=mode,
            host_header=host_header,
            extensions=extensions,
            domain=domain,
            append_domain=append_domain,
            status_codes_blacklist=status_codes_blacklist,
            exclude_status=exclude_status,
            threads=threads,
        )

        self.parser = GobusterParser()

    def collect(self):
        return self.adapter.execute()

    def normalize(self, raw_data):
        return self.parser.parse(
            raw_data,
            base_url=self.target,
        )

    def emit(self, observations):
        return {
            "sensor": self.name,
            "target": self.target,
            "observations": len(observations) if observations else 0,
        }
