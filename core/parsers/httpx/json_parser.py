from core.models.httpx_observation import HttpxObservation


class HttpxJsonParser:
    """
    Converts raw HTTPX JSON into canonical HttpxObservation objects.
    """

    def parse(self, records: list[dict]) -> list[HttpxObservation]:
        observations = []

        for record in records:
            observations.append(
                HttpxObservation(
                    url=record.get("url"),
                    host=record.get("host"),
                    host_ip=record.get("host_ip"),
                    port=int(record["port"]) if record.get("port") else None,
                    scheme=record.get("scheme"),
                    status_code=record.get("status_code"),
                    title=record.get("title"),
                    webserver=record.get("webserver"),
                    content_type=record.get("content_type"),
                    path=record.get("path"),
                    response_time=record.get("time"),
                    content_length=record.get("content_length"),
                    technologies=record.get("tech", []),
                    ipv4_addresses=record.get("a", []),
                    ipv6_addresses=record.get("aaaa", []),
                )
            )

        return observations