from cli.observer_dashboard import ObserverDashboard


class ObserverShell:
    """
    Interactive Observer shell.

    Maintains mission context after a strike and routes
    Observer commands without performing intelligence itself.
    """

    def __init__(self, context: dict | None = None):
        self.context = context or {}
        self.dashboard = ObserverDashboard()

    def run(self):
        self.dashboard.render(self.context)

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

            if not command:
                continue

            if command == "help":
                self.show_help()

            elif command == "status":
                self.dashboard.render(self.context)

            elif command == "hunter":
                self.show_hunter()

            elif command == "clear":
                self.dashboard.render(self.context)

            else:
                print()
                print(f"Unknown command: {command}")
                print("Type 'help' to view available commands.")
                print()

    def show_help(self):
        print()
        print("Available Commands")
        print("------------------")
        print("status   Show the Observatory dashboard")
        print("hunter   Show Hunter's assessment")
        print("clear    Redraw the Observatory")
        print("help     Show available commands")
        print("exit     Dismiss the Council")
        print()

    def show_hunter(self):
        leads = self.context.get("hunter_leads", [])

        print()
        print("══════════════════════════════════════")
        print("          HUNTER ASSESSMENT")
        print("══════════════════════════════════════")
        print()

        if not leads:
            print("No investigative leads identified.")
            print()
            return

        for index, lead in enumerate(leads, start=1):
            print(f"{index}. {lead}")

        print()