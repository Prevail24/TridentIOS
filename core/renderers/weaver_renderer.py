from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class WeaverRenderer:

    def render(self, report):

        console.print()

        console.print(
            Panel.fit(
                "[bold cyan]🕸️ The Weaver[/bold cyan]\n"
                "[italic]Relationship Analysis[/italic]",
                border_style="cyan",
            )
        )

        table = Table(show_header=False, box=None)

        table.add_row("Object", report.object_id)
        table.add_row("Type", report.object_type)
        table.add_row("Evidence", str(report.evidence_count))
        table.add_row("Notes", str(report.note_count))

        console.print(table)

        console.print()

        console.print(report.summary)