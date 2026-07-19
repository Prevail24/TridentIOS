from urllib.parse import quote, urljoin

from core.services.http_download_service import HttpDownloadService


def build_upload_url(base_url: str, filename: str) -> str:
    normalized = base_url

    if "://" not in normalized:
        normalized = f"http://{normalized}"

    quoted_filename = quote(filename.strip("/"), safe="")
    return urljoin(normalized.rstrip("/") + "/", f"uploads/{quoted_filename}")


def fetch_http_artifact(
    url: str,
    *,
    host_header: str | None = None,
) -> dict:
    return HttpDownloadService().run(
        url,
        host_header=host_header,
    )


def fetch_uploaded_artifact(
    base_url: str,
    filename: str,
    *,
    host_header: str | None = None,
) -> dict:
    return fetch_http_artifact(
        build_upload_url(base_url, filename),
        host_header=host_header,
    )


def print_http_artifact_result(result: dict) -> None:
    tool_run = result["tool_run"]
    observations = result["observations"]

    print("Artifact retrieval complete.")
    print(f"Run          : {tool_run.id}")
    print(f"Observations : {len(observations)}")

    for observation in observations:
        data = observation.data

        print()
        print(data["filename"])
        print(f"  Source   : {data['source_url']}")
        print(f"  Evidence : {data['evidence_path']}")
        print(f"  SHA256   : {data['sha256']}")
        print(f"  Size     : {data['size']}")

        if data["content_type"]:
            print(f"  Type     : {data['content_type']}")

    print()
