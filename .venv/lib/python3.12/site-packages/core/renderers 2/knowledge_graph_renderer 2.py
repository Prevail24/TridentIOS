class KnowledgeGraphRenderer:

    def render(self, graph):

        print()
        print("═══════════════════════════════════════")
        print("          KNOWLEDGE GRAPH")
        print("═══════════════════════════════════════")
        print()

        for edge in graph.edges:
            print(
                f"{edge.source.entity_type.upper()} "
                f"({edge.source.value})"
            )

            print(f"   └── {edge.relationship}")

            print(
                f"         {edge.target.entity_type.upper()} "
                f"({edge.target.value})"
            )

            print()