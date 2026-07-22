from core.armory.http_download.sensor import HttpDownloadSensor


class HttpDownloadService:
    """
    Compatibility facade for HTTP artifact retrieval.
    """

    def run(
        self,
        url: str,
        *,
        host_header: str | None = None,
    ):
        return HttpDownloadSensor(
            url,
            host_header=host_header,
        ).collect()
