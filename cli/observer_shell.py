from cli.observer_dashboard import ObserverDashboard
from core.kernel.mission_context import MissionContext


class ObserverShell:
    """
    Interactive Observer shell.

    Maintains mission context after a strike and routes
    Observer commands without performing intelligence itself.
    """

    def __init__(self, context: dict | None = None):
        self.context = context or {}
        self.mission_context = MissionContext()
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

            elif command == "runs":
                self.show_runs()

            elif command == "ports":
                self.show_ports()

            elif command == "services":
                self.show_services()
            
            elif command == "web":
                self.show_web()

            elif command == "all":
                self.show_all()

            else:
                print()
                print(f"Unknown command: {command}")
                print("Type 'help' to view available commands.")
                print()

    def show_help(self):
        print()
        print("Available Commands")
        print("------------------")
        print("status    Show the Observatory dashboard")
        print("all       Show the complete mission intelligence view")
        print("ports     Show open ports for the active mission")
        print("services  Show discovered network services")
        print("web       Show discovered HTTP surfaces")
        print("runs      Show tool runs for the active mission")
        print("hunter    Show Hunter's assessment")
        print("clear     Redraw the Observatory")
        print("help      Show available commands")
        print("exit      Dismiss the Council")
        print()

    def show_ports(self):
        print()
        print("══════════════════════════════════════")
        print("              OPEN PORTS")
        print("══════════════════════════════════════")
        print()

        try:
            ports = self.mission_context.open_ports()
        except RuntimeError as exc:
            print(str(exc))
            print()
            return

        if not ports:
            print("No open ports recorded for the active mission.")
            print()
            return

        for item in ports:
            endpoint = f"{item['port']}/{item['protocol']}"

            print(endpoint)
            print(f"  Host     : {item['host']}")
            print(f"  Service  : {item['service']}")

            if item["product"]:
                print(f"  Product  : {item['product']}")

            if item["version"]:
                print(f"  Version  : {item['version']}")

            if item["extrainfo"]:
                print(f"  Extra    : {item['extrainfo']}")

            print()

    def show_services(self):
        print()
        print("══════════════════════════════════════")
        print("              SERVICES")
        print("══════════════════════════════════════")
        print()

        try:
            services = self.mission_context.services()
        except RuntimeError as exc:
            print(str(exc))
            print()
            return

        if not services:
            print("No services recorded.")
            print()
            return

        for service in services:
            ports = ", ".join(
                str(port)
                for port in service["ports"]
            )

            print(service["service"])

            if service["product"]:
                print(f"  Product : {service['product']}")

            if service["version"]:
                print(f"  Version : {service['version']}")

            print(f"  Ports   : {ports}")
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

    def show_runs(self):
        print()
        print("══════════════════════════════════════")
        print("              TOOL RUNS")
        print("══════════════════════════════════════")
        print()

        try:
            runs = self.mission_context.runs()
        except RuntimeError as exc:
            print(str(exc))
            print()
            return

        if not runs:
            print("No tool runs recorded for the active mission.")
            print()
            return

        for run in runs:
            print(run.id)
            print(f"  Tool         : {run.tool}")
            print(f"  Target       : {run.target}")
            print(f"  Status       : {run.status}")
            print(f"  Observations : {len(run.observations)}")
            print(f"  Evidence     : {len(run.evidence)}")

            if run.started:
                print(f"  Started      : {run.started}")

            if run.finished:
                print(f"  Finished     : {run.finished}")

            print()

    def show_web(self):
            print()
            print("══════════════════════════════════════")
            print("            HTTP SURFACE")
            print("══════════════════════════════════════")
            print()

            try:
                surfaces = self.mission_context.web_surfaces()
            except RuntimeError as exc:
                print(str(exc))
                print()
                return

            if not surfaces:
                print("No HTTP surfaces recorded for the active mission.")
                print()
                return

            for surface in surfaces:
                print(surface["url"])

                if surface["status_code"] is not None:
                    print(f"  Status       : {surface['status_code']}")

                if surface["title"]:
                    print(f"  Title        : {surface['title']}")

                if surface["webserver"]:
                    print(f"  Web Server   : {surface['webserver']}")

                if surface["host_ip"]:
                    print(f"  IP Address   : {surface['host_ip']}")

                if surface["port"] is not None:
                    print(f"  Port         : {surface['port']}")

                if surface["content_type"]:
                    print(f"  Content Type : {surface['content_type']}")

                if surface["response_time"]:
                    print(f"  Response     : {surface['response_time']}")

                if surface["content_length"] is not None:
                    print(f"  Length       : {surface['content_length']}")

                if surface["technologies"]:
                    technologies = ", ".join(surface["technologies"])
                    print(f"  Technologies : {technologies}")

                print()   

    def show_all(self):
        print()
        print("══════════════════════════════════════")
        print("       MISSION INTELLIGENCE VIEW")
        print("══════════════════════════════════════")
        print()

        mission_id = self.mission_context.current_mission_id()

        print("Mission")
        print("--------------------------------------")
        print(f"Mission ID : {mission_id or 'None'}")
        print(f"Target     : {self.context.get('host', 'Unknown')}")
        print(f"Case       : {self.context.get('case_id', 'Unknown')}")
        print()

        self.show_ports()
        self.show_services()
        self.show_web()
        self.show_hunter()
        self.show_runs() 