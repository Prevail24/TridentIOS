from rich.console import Console
from rich.rule import Rule

console = Console()


class StrikeRenderer:
    """
    Live renderer for Medusa Strike.

    Owns the presentation of an active strike.
    Sensors emit events.
    Hunter emits intelligence.
    StrikeRenderer tells the story.
    """

    def header(self, target: str, case_id: str):
        console.print()
        console.print(Rule("[bold green]🐍 MEDUSA STRIKE"))
        console.print(f"[bold]Mission[/bold] : {case_id}")
        console.print(f"[bold]Target [/bold] : {target}")
        console.print()

    def council_online(self):
        console.print("[cyan]👁 Sentinel[/cyan]     Watching target...")
        console.print("[yellow]🎯 Hunter[/yellow]      Awaiting observations...")
        console.print("[green]📢 Reporter[/green]    Recording evidence...")
        console.print("[magenta]📚 Historian[/magenta]  Opening mission archive...")
        console.print("[blue]🔮 Oracle[/blue]       Pattern engine ready...")
        console.print("[red]⚖ Skeptic[/red]      Verification enabled...")
        console.print()

    def sensor_started(self, name: str):
        console.print(f"[cyan]▶[/cyan] {name}")

    def sensor_finished(self, name: str, summary: str = ""):
        if summary:
            console.print(f"[green]✓[/green] {name} — {summary}")
        else:
            console.print(f"[green]✓[/green] {name}")

    def hunter(self, message: str):
        console.print(f"[yellow]Hunter[/yellow] :: {message}")

    def reporter(self, message: str):
        console.print(f"[green]Reporter[/green] :: {message}")

    def historian(self, message: str):
        console.print(f"[magenta]Historian[/magenta] :: {message}")

    def briefing(self):
        console.print()
        console.print(Rule("[bold blue]MISSION BRIEFING"))