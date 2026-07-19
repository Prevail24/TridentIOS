from core.adapters.http_download_adapter import HttpDownloadAdapter
from core.armory.sensor import Sensor


class HttpDownloadSensor(Sensor):
    name = "http_download"
    version = "0.1.0"

    produces = [
        "http_artifact",
        "url",
        "filename",
        "content_type",
        "sha256",
    ]

    def __init__(
        self,
        url: str,
        *,
        host_header: str | None = None,
    ):
        self.url = url
        self.host_header = host_header
        self.adapter = HttpDownloadAdapter(
            url,
            host_header=host_header,
        )

    def collect(self):
        return self.adapter.execute()

    def normalize(self, raw_data):
        return raw_data

    def emit(self, observations):
        return {
            "sensor": self.name,
            "target": self.url,
            "observations": len(observations) if observations else 0,
        }
