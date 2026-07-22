import shlex

from cli.commands.http_artifact import (
    build_upload_url,
    fetch_http_artifact,
    fetch_uploaded_artifact,
    print_http_artifact_result,
)
from cli.observer_dashboard import ObserverDashboard
from core.kernel.mission_context import MissionContext
from core.services.gobuster_service import GobusterService
from core.planner.planner import Planner
from core.renderers.planner_renderer import PlannerRenderer
from core.command.capability_router import (
    CapabilityExecutionError,
    CapabilityNotFoundError,
    CapabilityRouter,
)
from core.species.web.web_species import WebSpecies


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
                raw_command = input("Observer> ").strip()
                command = raw_command.lower()
            except (KeyboardInterrupt, EOFError):
                raw_command = "exit"
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

            elif command == "vhosts":
                self.show_vhosts()

            elif command.startswith("gobuster"):
                self.run_gobuster(raw_command)

            elif command.startswith("vhost"):
                self.run_vhost(raw_command)

            elif command.startswith("download"):
                self.run_download(raw_command)

            elif command.startswith("fetch-upload"):
                self.run_fetch_upload(raw_command)

            elif command == "observations":
                self.show_observations()

            elif command == "ports":
                self.show_ports()

            elif command == "services":
                self.show_services()

            elif command == "web":
                self.show_web()

            elif command.startswith("plan execute"):
                self.execute_plan_recommendation(raw_command)

            elif command == "plan":
                self.show_plan()

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
        print("plan      Show the current mission plan")
        print("plan execute <number>")
        print("          Execute a ready recommendation after confirmation")

        print("ports     Show open ports for the active mission")
        print("services  Show discovered network services")
        print("web       Show discovered HTTP surfaces")
        print("vhosts    Show discovered virtual hosts")
        print("observations  Show canonical mission observations")
        print("gobuster <wordlist>")
        print("          Discover web content on the mission target")
        print("gobuster <target> <wordlist> [--host <host>] [--extensions <exts>]")
        print("          Discover web content with optional Host header/extensions")
        print("vhost <target> <domain> <wordlist> [--exclude-status <codes>]")
        print("          Discover virtual hosts for a domain")
        print("download <url>")
        print("          Retrieve an HTTP artifact into mission evidence")
        print("fetch-upload <base-url> <filename> [--host <host>]")
        print("          Retrieve a known file from /uploads into mission evidence")


        print("runs      Show tool runs for the active mission")
        print("hunter    Show Hunter's assessment")

        print("clear     Redraw the Observatory")
        print("help      Show available commands")
        print("exit      Dismiss the Council")
        print()

    def show_observations(self):
        print()
        print("══════════════════════════════════════")
        print("          OBSERVATIONS")
        print("══════════════════════════════════════")
        print()

        try:
            observations = self.mission_context.mission_observations()
        except RuntimeError as exc:
            print(str(exc))
            print()
            return

        if not observations:
            print("No observations recorded.")
            print()
            return

        for observation in observations:

            print(observation.id)
            print(f"  Category     : {observation.category}")

            if observation.tool_run_id:
                print(f"  Tool Run     : {observation.tool_run_id}")

            if observation.evidence_id:
                print(f"  Evidence     : {observation.evidence_id}")

            print(f"  Confidence   : {observation.confidence}")
            print(f"  Observed     : {observation.observed_at}")
            print()

            data = observation.data or {}

            for key in sorted(data.keys()):
                value = data[key]

                if isinstance(value, list):
                    value = ", ".join(str(v) for v in value)

                print(f"    {key:<16}: {value}")

            print()
            print("──────────────────────────────────────")
            print()

    def run_download(self, raw_command: str):
        """
        Retrieve an HTTP artifact and attach it to the active mission.

        Usage:
            download <url>
            download <url> <host-header>
        """
        parts = raw_command.split()

        if len(parts) == 2:
            url = parts[1]
            host_header = None

        elif len(parts) == 3:
            url = parts[1]
            host_header = parts[2]

        else:
            print()
            print("Usage:")
            print("  download <url>")
            print("  download <url> <host-header>")
            print()
            return

        print()
        print("Medusa")
        print(f"Retrieving artifact from {url}...")
        print()

        try:
            result = fetch_http_artifact(
                url,
                host_header=host_header,
            )
        except Exception as exc:
            print(f"Artifact retrieval failed: {exc}")
            print()
            return

        self.record_http_artifact_result(result)
        print_http_artifact_result(result)

    def run_fetch_upload(self, raw_command: str):
        """
        Retrieve a known uploaded file and attach it to the active mission.

        Usage:
            fetch-upload <base-url> <filename>
            fetch-upload <base-url> <filename> --host <host-header>
        """
        try:
            parts = shlex.split(raw_command)
        except ValueError as exc:
            print(f"Could not parse command: {exc}")
            print()
            return

        host_header = None

        if "--host" in parts:
            host_index = parts.index("--host")

            if host_index + 1 >= len(parts):
                print("Usage: fetch-upload <base-url> <filename> --host <host-header>")
                print()
                return

            host_header = parts[host_index + 1]
            del parts[host_index : host_index + 2]

        if len(parts) != 3:
            print()
            print("Usage:")
            print("  fetch-upload <base-url> <filename>")
            print("  fetch-upload <base-url> <filename> --host <host-header>")
            print()
            return

        _, base_url, filename = parts
        url = build_upload_url(base_url, filename)

        print()
        print("Medusa")
        print(f"Retrieving uploaded artifact from {url}...")
        print()

        try:
            result = fetch_uploaded_artifact(
                base_url,
                filename,
                host_header=host_header,
            )
        except Exception as exc:
            print(f"Uploaded artifact retrieval failed: {exc}")
            print()
            return

        self.record_http_artifact_result(result)
        print_http_artifact_result(result)

    def record_http_artifact_result(self, result: dict):
        tool_run = result["tool_run"]
        observations = result["observations"]

        self.context["http_download_run_id"] = tool_run.id
        self.context["http_artifacts"] = (
            self.context.get("http_artifacts", 0)
            + len(observations)
        )

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

                if surface["host_header"]:
                    print(f"  Host Header  : {surface['host_header']}")

                if surface["probe_url"]:
                    print(f"  Probe URL    : {surface['probe_url']}")

                if surface["status_code"] is not None:
                    print(f"  Status       : {surface['status_code']}")

                if surface["redirect_location"]:
                    print(
                        "  Redirect     : "
                        f"{surface['redirect_location']}"
                    )

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

    def show_vhosts(self):
            print()
            print("══════════════════════════════════════")
            print("          VIRTUAL HOSTS")
            print("══════════════════════════════════════")
            print()

            try:
                vhosts = self.mission_context.web_vhosts()
            except RuntimeError as exc:
                print(str(exc))
                print()
                return

            if not vhosts:
                print("No virtual hosts recorded for the active mission.")
                print()
                return

            for vhost in vhosts:
                print(vhost["hostname"])

                if vhost["url"]:
                    print(f"  URL      : {vhost['url']}")

                if vhost["base_url"]:
                    print(f"  Found Via: {vhost['base_url']}")

                if vhost["status_code"] is not None:
                    print(f"  Status   : {vhost['status_code']}")

                if vhost["content_length"] is not None:
                    print(f"  Length   : {vhost['content_length']}")

                if vhost["redirect_location"]:
                    print(f"  Redirect : {vhost['redirect_location']}")

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
        self.show_vhosts()
        self.show_hunter()
        self.show_runs()


    def run_gobuster(self, raw_command: str):
        """
        Deploy Gobuster against the current mission target.

        Usage:
            gobuster <wordlist>
            gobuster <target> <wordlist>
            gobuster <target> <wordlist> --host <host-header>
            gobuster <target> <wordlist> --extensions php,txt,bak
        """
        try:
            parts = shlex.split(raw_command)
        except ValueError as exc:
            print()
            print(f"Unable to parse command: {exc}")
            print()
            return

        try:
            positionals, options = self._parse_options(
                parts[1:],
                value_options={
                    "--host",
                    "--extensions",
                    "-x",
                    "--blacklist",
                    "--threads",
                },
            )
        except ValueError as exc:
            print()
            print(str(exc))
            print()
            return

        if len(positionals) == 1:
            target = self.context.get("host")
            wordlist = positionals[0]

        elif len(positionals) == 2:
            target = positionals[0]
            wordlist = positionals[1]

        else:
            print()
            print("Usage:")
            print("  gobuster <wordlist>")
            print("  gobuster <target> <wordlist>")
            print("  gobuster <target> <wordlist> --host <host-header>")
            print("  gobuster <target> <wordlist> --extensions php,txt,bak")
            print()
            return

        if not target:
            print()
            print("No mission target is available.")
            print("Provide one explicitly:")
            print("  gobuster <target> <wordlist>")
            print()
            return

        print()
        print("🐍 Medusa")
        print(f"Deploying Gobuster against {target}...")
        print()

        host_header = options.get("--host")
        extensions = options.get("--extensions") or options.get("-x")
        status_codes_blacklist = options.get("--blacklist", "302,404")

        try:
            threads = int(options.get("--threads", "10"))
        except ValueError:
            print("--threads must be an integer.")
            print()
            return

        try:
            result = GobusterService().run(
                target=target,
                wordlist=wordlist,
                host_header=host_header,
                extensions=extensions,
                status_codes_blacklist=status_codes_blacklist,
                threads=threads,
            )
        except FileNotFoundError as exc:
            print(f"Gobuster could not be deployed: {exc}")
            print()
            return
        except Exception as exc:
            print(f"Gobuster operation failed: {exc}")
            print()
            return

        tool_run = result["tool_run"]
        observations = result["observations"]

        self.context["gobuster_run_id"] = tool_run.id
        self.context["gobuster_observations"] = len(observations)

        print("Gobuster operation complete.")
        print(f"Run          : {tool_run.id}")
        print(f"Target       : {target}")
        print(f"Observations : {len(observations)}")
        print()

        for observation in observations:
            data = observation.data

            print(data["url"])
            print(f"  Path   : {data['path']}")

            if data["status_code"] is not None:
                print(f"  Status : {data['status_code']}")

            if data["content_length"] is not None:
                print(f"  Length : {data['content_length']}")

            if data["redirect_location"]:
                print(f"  Redirect: {data['redirect_location']}")

            print()

    def run_vhost(self, raw_command: str):
        """
        Discover virtual hosts for a domain.

        Usage:
            vhost <target> <domain> <wordlist>
            vhost <target> <domain> <wordlist> --exclude-status 301
        """
        try:
            parts = shlex.split(raw_command)
        except ValueError as exc:
            print()
            print(f"Unable to parse command: {exc}")
            print()
            return

        try:
            positionals, options = self._parse_options(
                parts[1:],
                value_options={
                    "--exclude-status",
                    "--threads",
                },
            )
        except ValueError as exc:
            print()
            print(str(exc))
            print()
            return

        if len(positionals) != 3:
            print()
            print("Usage:")
            print("  vhost <target> <domain> <wordlist>")
            print("  vhost <target> <domain> <wordlist> --exclude-status 301")
            print()
            return

        target, domain, wordlist = positionals
        exclude_status = options.get("--exclude-status")

        try:
            threads = int(options.get("--threads", "10"))
        except ValueError:
            print("--threads must be an integer.")
            print()
            return

        print()
        print("🐍 Medusa")
        print(f"Discovering virtual hosts for {domain} via {target}...")
        print()

        try:
            result = GobusterService().run(
                target=target,
                wordlist=wordlist,
                mode="vhost",
                domain=domain,
                append_domain=True,
                exclude_status=exclude_status,
                threads=threads,
            )
        except FileNotFoundError as exc:
            print(f"Gobuster vhost could not be deployed: {exc}")
            print()
            return
        except Exception as exc:
            print(f"Gobuster vhost operation failed: {exc}")
            print()
            return

        tool_run = result["tool_run"]
        observations = result["observations"]

        self.context["vhost_run_id"] = tool_run.id
        self.context["vhost_observations"] = len(observations)

        print("Virtual host discovery complete.")
        print(f"Run          : {tool_run.id}")
        print(f"Target       : {target}")
        print(f"Domain       : {domain}")
        print(f"Observations : {len(observations)}")
        print()

        for observation in observations:
            data = observation.data

            print(data["hostname"])

            if data["status_code"] is not None:
                print(f"  Status : {data['status_code']}")

            if data["content_length"] is not None:
                print(f"  Length : {data['content_length']}")

            if data["redirect_location"]:
                print(f"  Redirect: {data['redirect_location']}")

            print()

    def show_plan(self):
        try:
            planner = Planner()
            recommendations = planner.plan(self.mission_context)
        except RuntimeError as exc:
            print()
            print(str(exc))
            print()
            return

        PlannerRenderer().render(recommendations)

    def execute_plan_recommendation(
        self,
        raw_command: str,
    ):
        """
        Execute a numbered Planner recommendation after explicit
        operator confirmation.

        Usage:
            plan execute <number>
        """
        try:
            parts = shlex.split(raw_command)
        except ValueError as exc:
            print()
            print(f"Could not parse command: {exc}")
            print()
            return

        if len(parts) != 3:
            print()
            print("Usage: plan execute <number>")
            print()
            return

        try:
            selection = int(parts[2])
        except ValueError:
            print()
            print("Recommendation number must be an integer.")
            print()
            return

        if selection < 1:
            print()
            print("Recommendation number must be 1 or greater.")
            print()
            return

        try:
            recommendations = Planner().plan(
                self.mission_context
            )
        except RuntimeError as exc:
            print()
            print(str(exc))
            print()
            return

        if not recommendations:
            print()
            print("No recommendations are currently available.")
            print()
            return

        if selection > len(recommendations):
            print()
            print(
                f"Recommendation {selection} does not exist. "
                f"Choose a number from 1 to "
                f"{len(recommendations)}."
            )
            print()
            return

        recommendation = recommendations[selection - 1]

        print()
        print("Selected Recommendation")
        print("-----------------------")
        print(recommendation.capability_id)
        print(f"Reason: {recommendation.reason}")

        if not recommendation.executable:
            print()
            print("This recommendation is not ready to execute.")

            if not recommendation.available:
                print("The capability is currently unavailable.")

            if recommendation.required_inputs:
                required = ", ".join(
                    recommendation.required_inputs
                )
                print(f"Missing input: {required}")

            print()
            return

        print()
        confirmation = input(
            "Execute this recommendation? [y/N]: "
        ).strip().lower()

        if confirmation not in {"y", "yes"}:
            print()
            print("Execution cancelled.")
            print()
            return

        router = CapabilityRouter(
            WebSpecies().serpents()
        )

        print()
        print("Medusa")
        print(
            f"Dispatching {recommendation.capability_id}..."
        )
        print()

        try:
            router.execute_recommendation(
                recommendation,
                self.mission_context,
            )
        except (
            CapabilityExecutionError,
            CapabilityNotFoundError,
            RuntimeError,
        ) as exc:
            print(f"Execution failed: {exc}")
            print()
            return

        print("Capability execution completed.")
        print()
        print("Updated mission plan:")

        self.show_plan()

    def _parse_options(
        self,
        tokens: list[str],
        *,
        value_options: set[str],
    ) -> tuple[list[str], dict[str, str]]:
        positionals = []
        options = {}
        index = 0

        while index < len(tokens):
            token = tokens[index]

            if token in value_options:
                if index + 1 >= len(tokens):
                    raise ValueError(f"{token} requires a value.")

                options[token] = tokens[index + 1]
                index += 2
                continue

            if token.startswith("--") or token.startswith("-"):
                raise ValueError(f"Unknown option: {token}")

            positionals.append(token)
            index += 1

        return positionals, options
