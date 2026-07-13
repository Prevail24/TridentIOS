class ObserverShell:
    """
    Interactive Observer shell.

    Maintains mission context after a strike.
    """

    def __init__(self, context: dict | None = None):
        self.context = context or {}

    def run(self):
        print()
        print("══════════════════════════════════════")
        print("        OBSERVER CONSOLE")
        print("══════════════════════════════════════")
        print()
        print("Type 'help' to view commands.")
        print()

        while True:
            try:
                command = input("Observer> ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                command = "exit"

            if command in ("exit", "quit"):
                print()
                print("🐍 Medusa")
                print("Council dismissed.")
                print()
                break

            if command == "help":
                self.help()
            elif command == "status":
                self.status()
            elif command == "hunter":
                self.hunter()
            elif command == "clear":
                print("\033c", end="")
            elif not command:
                continue
            else:
                print(f"Unknown command: {command}")

    def help(self):
        print()
        print("Observer Commands")
        print("-----------------")
        print("status     View current mission")
        print("help       Show this menu")
        print("clear      Clear the screen")
        print("exit       Leave the Observatory")
        print()

    def status(self):
        print()
        print("═══════════════════════════════")
        print("        MISSION STATUS")
        print("═══════════════════════════════")
        print()

        print(f"Case ID      : {self.context.get('case_id', 'None')}")
        print(f"Run ID       : {self.context.get('run_id', 'None')}")
        print(f"Target       : {self.context.get('host', 'None')}")
        print(f"Status       : ACTIVE")

        leads = self.context.get("hunter_leads", [])

        print(f"Hunter Leads : {len(leads)}")
        print()

    def hunter(self):
        print()
        print("═══════════════════════════════")
        print("      HUNTER ASSESSMENT")
        print("═══════════════════════════════")
        print()

        leads = self.context.get("hunter_leads", [])

        if not leads:
            print("No investigative leads identified.")
            print()
            return

        for index, lead in enumerate(leads, start=1):
            print(f"{index}. {lead}")

        print()