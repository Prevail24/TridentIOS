from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.config import Config

console = Console()


class MissionRenderer:
    def render(self, mission):
        console.print()

        console.print(
            Panel.fit(
                "[bold cyan]🔱 Mission Overview[/bold cyan]",
                border_style="cyan",
            )
        )

        console.rule("[cyan]Operation")

        table = Table(show_header=False, box=None)

        table.add_row("[bold]Mission[/bold]", mission.title)
        table.add_row("[bold]Mission ID[/bold]", mission.id)
        table.add_row("[bold]Status[/bold]", f"🟢 {mission.status.upper()}")
        table.add_row("[bold]Priority[/bold]", mission.priority.upper())
        table.add_row("[bold]Operator[/bold]", mission.operator)
        console.print(table)
        console.print()

        console.rule("[cyan]Intelligence Summary")

        summary = Table(show_header=False, box=None)
        summary.add_row("[bold]Entities[/bold]", "0")
        summary.add_row("[bold]Observations[/bold]", str(len(mission.observations)))
        summary.add_row("[bold]Evidence[/bold]", "0")
        summary.add_row("[bold]Relationships[/bold]", "0")
        console.print(summary)

        console.print()
        console.rule("[cyan]Operational State")

        ops = Table(show_header=False, box=None)
        ops.add_row("[bold]Workspace[/bold]", f"missions/{mission.id}/")
        ops.add_row("[bold]Loom Status[/bold]", "READY")
        ops.add_row("[bold]Next Command[/bold]", "trident observation create")
        console.print(ops)

        console.print()
        console.print(f"[italic dim]{Config.BRAND_QUOTE}[/italic dim]")