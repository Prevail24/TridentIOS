from core.armory.sensor import Sensor
from core.armory.web_inspector.adapter import WebInspectorAdapter
from core.parsers.web_inspector.html_parser import (
    WebInspectorHtmlParser,
)


class WebInspectorSensor(Sensor):
    name = "web_inspector"
    version = "0.1.0"

    produces = [
        "web_page",
        "headers",
        "cookies",
        "links",
        "forms",
        "scripts",
        "comments",
        "metadata",
    ]

    def __init__(
        self,
        target: str,
        *,
        timeout: float = 10.0,
        follow_redirects: bool = True,
        verify_tls: bool = True,
    ):
        self.target = target

        self.adapter = WebInspectorAdapter(
            target=target,
            timeout=timeout,
            follow_redirects=follow_redirects,
            verify_tls=verify_tls,
        )

        self.parser = WebInspectorHtmlParser()

    def collect(self):
        return self.adapter.execute()

    def normalize(self, raw_data):
        return self.parser.parse(
            raw_data,
            requested_url=self.target,
        )

    def emit(self, observation):
        return {
            "sensor": self.name,
            "target": self.target,
            "status_code": observation.status_code,
            "title": observation.title,
            "links": len(observation.links),
            "forms": len(observation.forms),
            "scripts": len(observation.scripts),
            "comments": len(observation.comments),
        }
