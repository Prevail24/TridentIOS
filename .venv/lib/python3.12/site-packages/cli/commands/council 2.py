from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_council():

    table = Table(show_header=False, box=None)

    table.add_row("🐍", "[bold green]Medusa[/]", "ONLINE")
    table.add_row("👁", "Sentinel", "AWAKE")
    table.add_row("🎯", "Hunter", "AWAKE")
    table.add_row("📢", "Reporter", "AWAKE")
    table.add_row("📚", "Historian", "AWAKE")
    table.add_row("⚖", "Skeptic", "AWAKE")
    table.add_row("♞", "Strategist", "SLEEPING")
    table.add_row("🔮", "Oracle", "SLEEPING")

    console.print()

    console.print(
        Panel.fit(
            table,
            title="🔱 THE OBSERVATORY COUNCIL",
            border_style="green",
        )
    )

    console.print()

    console.print("[bold]Reality changes.[/]")
    console.print("Sentinel notices.")
    console.print("Hunter chooses.")
    console.print("Reporter informs.")
    console.print("Historian remembers.")
    console.print("Oracle predicts.")
    console.print("[bold green]Medusa coordinates.[/]")
    console.print("[bold cyan]The Observer decides.[/]")