from core.adapters.nmap_adapter import NmapAdapter


def recon_nmap(target: str):
    adapter = NmapAdapter(target)

    run = adapter.execute()

    print()
    print("═══════════════════════════════")
    print("      NMAP COMPLETE")
    print("═══════════════════════════════")
    print()
    print(f"Run ID : {run.id}")
    print(f"Target : {run.target}")
    print()