from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from core.config import Config

console = Console()


class TerminalRenderer:

    def banner(self, mission: str):

        console.print()

        console.print(
            Panel.fit(
                f"[bold cyan]⚓ {Config.APP_NAME}[/bold cyan]\n"
                "[green]The Observatory Terminal[/green]\n\n"
                f"[bold]Mission:[/bold] {mission}\n\n"
                f"[italic]{Config.BRAND_QUOTE}[/italic]",
                border_style="green",
            )
        )

    def observation_card(self, observation):

        table = Table(show_header=False, box=None)

        table.add_row("[bold]ID[/bold]", observation.id)
        table.add_row("[bold]Title[/bold]", observation.title)
        table.add_row("[bold]Platform[/bold]", observation.platform)
        table.add_row("[bold]Category[/bold]", observation.category)
        table.add_row("[bold]Difficulty[/bold]", observation.difficulty)
        table.add_row("[bold]Status[/bold]", observation.status)
        table.add_row("[bold]Observer[/bold]", observation.author)

        console.print()

        console.print(
            Panel(
                table,
                title="[bold cyan]Observation[/bold cyan]",
                border_style="green",
            )
        )

    def mission_card(self, mission):

        table = Table(show_header=False, box=None)

        table.add_row("[bold]ID[/bold]", mission.id)
        table.add_row("[bold]Title[/bold]", mission.title)
        table.add_row("[bold]Type[/bold]", mission.mission_type)
        table.add_row("[bold]Priority[/bold]", mission.priority)
        table.add_row("[bold]Status[/bold]", mission.status)
        table.add_row("[bold]Observer[/bold]", mission.observer)

        console.print()

        console.print(
            Panel(
                table,
                title="[bold cyan]Mission[/bold cyan]",
                border_style="green",
            )
        )

    def archive(self, observations):

        table = Table(
            title="Observation Archive",
            border_style="green",
            show_lines=False,
        )

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Title", style="white")
        table.add_column("Platform", style="green")
        table.add_column("Status", style="yellow")

        for observation in observations:
            table.add_row(
                observation.id,
                observation.title,
                observation.platform,
                observation.status.upper(),
            )

        console.print()
        console.print(table)

    def success(self, title: str, message: str):

        console.print()

        console.print()

        console.print(
            Panel.fit(
                f"[bold green]{title}[/bold green]\n\n{message}",
                border_style="green",
            )
        )

    def warning(self, title: str, message: str):

        console.print()

        console.print(
            Panel.fit(
                f"[bold yellow]{title}[/bold yellow]\n\n{message}",
                border_style="yellow",
            )
        )