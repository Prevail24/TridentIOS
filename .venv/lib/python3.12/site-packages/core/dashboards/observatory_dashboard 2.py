from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from core.config import Config
from core.services.mission_service import MissionService
from core.services.observation_service import ObservationService
from core.services.evidence_service import EvidenceService
from core.agents.weaver_brief import WeaverBrief

console = Console()


class ObservatoryDashboard:
    """
    Headquarters of The Watchers.

    This is the first screen every Observer sees.
    """

    def show(self):

        missions = MissionService().count()
        observations = ObservationService().count()
        evidence = EvidenceService().count()
        weaver = WeaverBrief().generate()

        console.print()

        console.print(
            Panel.fit(
                "[bold cyan]⚓ THE OBSERVATORY[/bold cyan]\n"
                "[italic]The Loom remembers what others forget.[/italic]",
                border_style="cyan",
            )
        )

        status = Table(show_header=False, box=None)

        status.add_row("Observer", "Prevail")
        status.add_row("Status", "[green]ONLINE[/green]")
        status.add_row("Knowledge Base", "ACTIVE")

        console.print(
            Panel.fit(
                f"""[bold cyan]🕸 THE WEAVER[/bold cyan]

        Health: [green]{weaver.health}[/green]

        Empty Observations : {weaver.empty_observations}

        Missing Missions   : {weaver.orphaned_observations}

        Duplicate Evidence : {weaver.duplicate_evidence}
        """,
                border_style="cyan",
            )
        )

        summary = Table(
            title="Knowledge Summary",
            show_header=False,
        )

        summary.add_row("Missions", str(missions))
        summary.add_row("Observations", str(observations))
        summary.add_row("Evidence", str(evidence))

        console.print(summary)

        console.rule("[cyan]Command Center")

        console.print(
            "[green]mission create[/green]"
        )

        console.print(
            "[green]mission open MIS-2026-0001[/green]"
        )

        console.print(
            "[green]observation create[/green]"
        )

        console.print(
            "[green]evidence create[/green]"
        )

        console.print(
            "[green]weaver analyze OBS-2026-0009[/green]"
        )

        console.print()

        console.print(
            f"[italic dim]{Config.BRAND_QUOTE}[/italic dim]"
        )