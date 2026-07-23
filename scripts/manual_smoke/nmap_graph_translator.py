from core.models.nmap_observation import NmapObservation
from core.services.nmap_observation_translator import NmapObservationTranslator


observations = [
    NmapObservation(
        host="45.33.32.156",
        port="22",
        protocol="tcp",
        state="open",
        service="ssh",
        product="OpenSSH",
        version="6.6.1p1 Ubuntu 2ubuntu2.13",
    ),
    NmapObservation(
        host="45.33.32.156",
        port="80",
        protocol="tcp",
        state="open",
        service="http",
        product="Apache httpd",
        version="2.4.7",
    ),
]

translator = NmapObservationTranslator()
graph = translator.build_graph(observations)

print()
print("NMAP GRAPH TRANSLATOR")
print("---------------------")
print(f"Nodes: {graph.node_count()}")
print(f"Edges: {graph.edge_count()}")