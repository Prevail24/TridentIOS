from rich.console import Console

from core.models.graph import GraphNode

console = Console()


class GraphRenderer:
    """
    Renders GraphNode trees.
    """

    def render(self, node: GraphNode):

        console.print()

        console.print("[bold cyan]⚓ THE CARTOGRAPHER[/bold cyan]")

        console.print()

        self._render_node(node)

        console.print()

    def _render_node(
        self,
        node: GraphNode,
        prefix: str = "",
        is_last: bool = True,
    ):

        connector = "└── " if is_last else "├── "

        console.print(f"{prefix}{connector}{node.label}")

        new_prefix = prefix + ("    " if is_last else "│   ")

        for index, child in enumerate(node.children):

            self._render_node(
                child,
                new_prefix,
                index == len(node.children) - 1,
            )