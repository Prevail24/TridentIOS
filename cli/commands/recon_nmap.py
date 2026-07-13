from cli.observer_shell import ObserverShell
from core.archive.case_manager import CaseManager
from core.renderers.strike_renderer import StrikeRenderer
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
    renderer = StrikeRenderer()

    # Nmap must complete before the Case can reference its primary run.
    renderer.sensor_started("Nmap")
    nmap_run = recon_nmap(target)
    renderer.sensor_finished(
        "Nmap",
        "Reconnaissance complete",
    )

    case = CaseManager().create_case(
        target=target,
        run_id=nmap_run.id,
    )

    renderer.header(
        target=target,
        case_id=case["case_id"],
    )
    renderer.council_online()

    # Launch HTTPX only when Nmap identifies a web-capable surface.
    httpx_result = None

    if has_web_surface(nmap_run):
        renderer.sensor_started("HTTPX")
        httpx_result = recon_httpx(target)

        if httpx_result:
            observation_count = len(httpx_result["observations"])
            renderer.sensor_finished(
                "HTTPX",
                f"{observation_count} observations collected",
            )
        else:
            renderer.reporter(
                "HTTPX failed or returned no usable results."
            )
    else:
        renderer.reporter(
            "No HTTP-capable surface detected. HTTPX deferred."
        )

    # Hunter evaluates the combined Nmap and HTTPX intelligence.
    hunter = Hunter()
    leads = hunter.hunt(target)

    if not leads:
        renderer.hunter(
            "No investigative leads identified."
        )
    else:
        renderer.hunter(
            f"{len(leads)} investigative leads generated."
        )

        for lead in leads:
            renderer.hunter(lead)

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

    renderer.briefing()
    renderer.reporter(
        "Initial reconnaissance complete. Observer assuming command."
    )

    print()
    print("═══════════════════════════════")
    print("   MISSION BRIEFING COMPLETE")
    print("═══════════════════════════════")
    print()
    print(f"Target       : {target}")
    print(f"Case         : {case['case_id']}")
    print(f"Nmap Run     : {nmap_run.id}")
    print(f"Hunter Leads : {len(leads)}")

    if httpx_result:
        print(f"HTTPX Run    : {httpx_result['tool_run'].id}")
        print(
            f"HTTPX Obs    : "
            f"{len(httpx_result['observations'])}"
        )

    print()
    input("Press ENTER to assume command... ")
    print()

    ObserverShell(context).run()


def recon_nmap(target: str):
    sensor = NmapSensor(target)
    return sensor.collect()


def has_web_surface(run) -> bool:
    """
    Return True when Nmap produced an open HTTP-capable service.
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

        if any(
            marker in service
            for marker in HTTP_SERVICE_MARKERS
        ):
            return True

    return False


def recon_httpx(target: str):
    try:
        return HttpxService().run(target)
    except FileNotFoundError:
        return None
    except Exception:
        return None