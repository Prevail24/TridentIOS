from rich.console import Console
from rich.panel import Panel

console = Console()


class EntityGraphRenderer:
    def render(self, graph):
        console.print()

        console.print(
            Panel.fit(
                f"[bold cyan]🕸 ENTITY GRAPH[/bold cyan]\n"
                f"[italic]{graph.center}[/italic]",
                border_style="cyan",
            )
        )

        if not graph.edges:
            console.print("No relationships found.")
            console.print()
            return

        for edge in graph.edges:
            console.print(f"[bold magenta]{edge.source}[/bold magenta]")
            console.print("   │")
            console.print(f"   ├── [yellow]{edge.relationship}[/yellow]")
            console.print("   │")
            console.print(f"   ▼")
            console.print(f"[bold magenta]{edge.target}[/bold magenta]")
            console.print()

        console.print()