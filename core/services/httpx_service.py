from core.armory.httpx.sensor import HttpxSensor


class HttpxService:
    """
    Compatibility facade for the HTTPX sensor pipeline.
    """

    def run(self, target: str):
        return HttpxSensor(target).collect()
