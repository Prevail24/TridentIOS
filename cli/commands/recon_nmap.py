from cli.observer_shell import ObserverShell
from core.archive.case_manager import CaseManager
from core.repositories.observation_repository import ObservationRepository
from core.sensors.nmap.sensor import NmapSensor
from core.serpents.hunter import Hunter
from core.services.httpx_service import HttpxService


HTTP_PORTS = {
    80,
    443,
    8000,
    8008,
    8080,
    8081,
    8443,
    8888,
    9000,
}

HTTP_SERVICE_MARKERS = {
    "http",
    "https",
    "http-proxy",
    "ssl/http",
}


def medusa_strike(target: str):
    print()
    print("🐍 Medusa")
    print("Council assembling...")
    print()
    print("👁 Sentinel  : Monitoring reality")
    print("🎯 Hunter    : Preparing investigation")
    print("📢 Reporter  : Standing by")
    print()
    print("Strike authorized.")
    print()

    # Foreground reconnaissance
    nmap_run = recon_nmap(target)

    # Create the case from the primary reconnaissance run.
    case = CaseManager().create_case(
        target=target,
        run_id=nmap_run.id,
    )

    # First sensor-trigger rule:
    # only launch HTTPX when Nmap found an HTTP-capable surface.
    httpx_result = None

    if has_web_surface(nmap_run):
        httpx_result = recon_httpx(target)
    else:
        print()
        print("HTTPX")
        print("-----")
        print("No HTTP-capable surface detected.")
        print("Sensor deferred.")
        print()

    # Hunter now evaluates after Nmap and HTTPX have populated the Loom.
    hunter = Hunter()
    leads = hunter.hunt(target)

    print()
    print("═══════════════════════════════")
    print("      HUNTER ASSESSMENT")
    print("═══════════════════════════════")
    print()

    if not leads:
        print("No investigative leads identified.")
    else:
        for index, lead in enumerate(leads, start=1):
            print(f"{index}. {lead}")

    context = {
        "host": target,
        "run_id": nmap_run.id,
        "case_id": case["case_id"],
        "hunter_leads": leads,
    }

    if httpx_result:
        httpx_run = httpx_result["tool_run"]
        httpx_observations = httpx_result["observations"]

        context["httpx_run_id"] = httpx_run.id
        context["httpx_observations"] = len(httpx_observations)

    ObserverShell(context).run()


def recon_nmap(target: str):
    sensor = NmapSensor(target)
    run = sensor.collect()

    print()
    print("═══════════════════════════════")
    print("      NMAP COMPLETE")
    print("═══════════════════════════════")
    print()
    print(f"Run ID : {run.id}")
    print(f"Target : {target}")
    print()

    return run


def has_web_surface(run) -> bool:
    """
    Determine whether Nmap produced an open HTTP-capable service.

    ToolRun stores observation IDs, so this function retrieves those
    canonical observations from the Loom and evaluates their data.
    """
    repository = ObservationRepository()

    for observation_id in run.observations:
        try:
            observation = repository.open(observation_id)
        except (FileNotFoundError, ValueError):
            continue

        data = observation.data or {}

        state = str(data.get("state", "")).lower()
        service = str(data.get("service", "")).lower()

        try:
            port = int(data.get("port"))
        except (TypeError, ValueError):
            port = None

        if state and state != "open":
            continue

        if port in HTTP_PORTS:
            return True

        if any(marker in service for marker in HTTP_SERVICE_MARKERS):
            return True

    return False


def recon_httpx(target: str):
    print()
    print("═══════════════════════════════")
    print("      HTTPX INITIATED")
    print("═══════════════════════════════")
    print()
    print(f"Target : {target}")
    print()

    try:
        result = HttpxService().run(target)
    except FileNotFoundError:
        print("HTTPX failed: executable not found.")
        print("Confirm ProjectDiscovery httpx is installed and on PATH.")
        print()
        return None
    except Exception as exc:
        print(f"HTTPX failed: {exc}")
        print()
        return None

    tool_run = result["tool_run"]
    observations = result["observations"]

    print()
    print("═══════════════════════════════")
    print("      HTTPX COMPLETE")
    print("═══════════════════════════════")
    print()
    print(f"Run ID       : {tool_run.id}")
    print(f"Target       : {target}")
    print(f"Observations : {len(observations)}")
    print()

    for observation in observations:
        data = observation.data or {}

        url = data.get("url", "Unknown")
        status = (
            data.get("status_code")
            or data.get("http_status")
            or "Unknown"
        )
        title = (
            data.get("title")
            or data.get("page_title")
            or "Untitled"
        )

        print(f"  {status}  {url}")
        print(f"       {title}")

    print()

    return result