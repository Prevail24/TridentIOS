from core.sensors.nmap.sensor import NmapSensor
from core.serpents.hunter import Hunter
from cli.observer_shell import ObserverShell
from core.archive.case_manager import CaseManager

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

    run = recon_nmap(target)
    case = CaseManager().create_case(
        target=target,
        run_id=run.id,

    )

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

    ObserverShell(
        {
        "host": target,
        "run_id": run.id,
        "case_id": case["case_id"],
        "hunter_leads": leads,
        }
    ).run()


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

    return run