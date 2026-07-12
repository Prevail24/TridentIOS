from rich.console import Console
from rich.panel import Panel

console = Console()


class AnalysisRenderer:

    def render(self, analysis):

        console.print()

        console.print(
            Panel.fit(
                "[bold green]🧠 THE ANALYST[/bold green]\n"
                f"[italic]{analysis['entity']}[/italic]",
                border_style="green",
            )
        )

        console.print()

        console.print(
            f"[bold]Connections[/bold] : {analysis['connections']}"
        )

        console.print()

        for edge in analysis["edges"]:

            console.print(
                f"• {edge.relationship} → {edge.target}"
            )

        console.print()