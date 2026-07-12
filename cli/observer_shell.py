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
            elif command == "clear":
                print("\033c", end="")
            elif not command:
                continue
            else:
                print(f"Unknown command: {command}")

    def help(self):
        print()
        print("Available Commands")
        print("------------------")
        print("status")
        print("help")
        print("clear")
        print("exit")
        print()

    def status(self):
        print()
        print("Mission Status")
        print("--------------")

        host = self.context.get("host")
        leads = self.context.get("hunter_leads", [])

        print(f"Target : {host or 'None'}")
        print(f"Leads  : {len(leads)}")
        print()