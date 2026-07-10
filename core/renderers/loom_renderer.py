class LoomRenderer:

    def render(self, graph):

        print()
        print("══════════════════════════════════════════════")
        print("                THE LOOM")
        print("══════════════════════════════════════════════")
        print()

        for edge in graph.edges:

            print(
                f"{edge.source.entity_type.upper()} "
                f"({edge.source.value})"
            )

            print(f"   │")

            print(f"   └── {edge.relationship}")

            print(f"         │")

            print(
                f"         └── "
                f"{edge.target.entity_type.upper()} "
                f"({edge.target.value})"
            )

            print()