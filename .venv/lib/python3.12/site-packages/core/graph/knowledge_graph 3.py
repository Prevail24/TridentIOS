from .edge import Edge


class KnowledgeGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        key = (node.entity_type, node.value)

        self.nodes[key] = node

        return node

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def node_count(self):
        return len(self.nodes)

    def edge_count(self):
        return len(self.edges)