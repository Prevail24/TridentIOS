from pathlib import Path

from core.parsers.nmap.xml_parser import NmapXMLParser


parser = NmapXMLParser()

xml = Path("knowledge/evidence/nmap/RUN-2026-0002.xml")

observations = parser.parse(xml)

print(f"\nFound {len(observations)} observations\n")

for obs in observations:
    print(
        f"{obs.host} "
        f"{obs.port}/{obs.protocol} "
        f"{obs.state} "
        f"{obs.service}"
    )