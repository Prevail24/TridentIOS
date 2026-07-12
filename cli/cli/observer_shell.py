class ObserverShell:
    """
    Interactive Observer shell.

    The shell maintains mission context after a strike
    and routes Observer commands to the appropriate
    Council members.
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

            elif command == "help":

                self.help()

            elif command == "status":

                self.status()

            elif command == "clear":

                print("\033c", end="")

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

        if host:
            print(f"Target : {host}")
        else:
            print("No active mission.")

        print()