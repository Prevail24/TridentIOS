from core.graph.graph_builder import GraphBuilder
from core.graph.loom_repository import LoomRepository

builder = GraphBuilder()

graph = builder.add_host_port_service(
    host_value="45.33.32.156",
    port_value="22",
    service_value="ssh",
    product_value="OpenSSH",
    version_value="6.6.1p1",
)

repo = LoomRepository("knowledge/loom/test_loom.json")
repo.save(graph)

loaded = repo.load()

print()
print("LOOM REPOSITORY")
print("---------------")
print(f"Nodes: {loaded.node_count()}")
print(f"Edges: {loaded.edge_count()}")