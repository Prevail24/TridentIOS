class ObserverDashboard:
    """
    Renders the Observatory Operations Console.

    Presentation only. No intelligence is performed here.
    """

    def render(self, context: dict):
        print("\033c", end="")

        host = context.get("host", "Unknown")
        leads = context.get("hunter_leads", [])

        print("╔════════════════════════════════════════════════════════════╗")
        print("║                        🐍 MEDUSA                           ║")
        print("║              Observatory Operations Console               ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print()

        print("Mission")
        print("────────────────────────────────────────────────────────────")
        print(f"Target      {host}")
        print("Status      ACTIVE")
        print()

        print("Council")
        print("────────────────────────────────────────────────────────────")
        print("👁 Sentinel      WATCHING")
        print("🎯 Hunter        READY")
        print("📢 Reporter      READY")
        print("📚 Historian     STANDBY")
        print("🔮 Oracle        STANDBY")
        print("⚖ Skeptic       STANDBY")
        print()

        print("Hunter")
        print("────────────────────────────────────────────────────────────")
        print(f"{len(leads)} investigative leads available.")
        print()

        print("────────────────────────────────────────────────────────────")
        print("Type 'help' to view commands.")
        print()