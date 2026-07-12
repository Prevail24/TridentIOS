from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class Dossier:

    def __init__(
        self,
        title: str,
        subtitle: str,
        color: str = "cyan",
        icon: str = "⚓",
    ):

        self.title = title
        self.subtitle = subtitle
        self.color = color
        self.icon = icon

        self.table = Table(
            show_header=False,
            box=None,
            pad_edge=False,
        )

    def add(self, key, value):

        self.table.add_row(
            f"[bold]{key}[/bold]",
            str(value),
        )

    def render(self):

        console.print()

        console.print(
            Panel.fit(
                f"[bold {self.color}]{self.icon} {self.title}[/bold {self.color}]\n"
                f"[italic]{self.subtitle}[/italic]",
                border_style=self.color,
            )
        )

        console.print(self.table)

        console.print()