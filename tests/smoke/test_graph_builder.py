from core.graph.graph_builder import GraphBuilder

builder = GraphBuilder()

graph = builder.add_host_port_service(
    host_value="45.33.32.156",
    port_value="22",
    service_value="ssh",
    product_value="OpenSSH",
    version_value="6.6.1p1 Ubuntu 2ubuntu2.13",
)

print()
print("GRAPH BUILDER")
print("-------------")
print(f"Nodes: {graph.node_count()}")
print(f"Edges: {graph.edge_count()}")