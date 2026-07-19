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
        status_codes_blacklist: str = "302,404",
        threads: int = 10,
    ):
        self.target = target
        self.wordlist = wordlist

        self.adapter = GobusterAdapter(
            target=target,
            wordlist=wordlist,
            status_codes_blacklist=status_codes_blacklist,
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
