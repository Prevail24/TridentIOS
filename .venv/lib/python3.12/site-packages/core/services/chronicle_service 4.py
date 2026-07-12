from collections import defaultdict

from core.services.timeline_service import TimelineService


class ChronicleService:
    """
    Converts a raw timeline into investigation events.
    """

    def __init__(self):
        self.timeline = TimelineService()

    def build(self, host: str):

        events = self.timeline.build(host)

        groups = defaultdict(list)

        #
        # Group observations by second.
        # (We'll later group by ToolRun/Mission.)
        #
        for event in events:
            timestamp = event["observed_at"].replace(microsecond=0)
            groups[timestamp].append(event)

        chronicle = []

        for timestamp in sorted(groups):

            observations = groups[timestamp]

            services = sorted({
                e["data"].get("service")
                for e in observations
                if e["data"].get("service")
            })

            products = sorted({
                e["data"].get("product")
                for e in observations
                if e["data"].get("product")
            })

            versions = sorted({
                e["data"].get("version")
                for e in observations
                if e["data"].get("version")
            })

            chronicle.append({
                "timestamp": timestamp,
                "services": services,
                "products": products,
                "versions": versions,
                "count": len(observations),
            })

        return chronicle
    