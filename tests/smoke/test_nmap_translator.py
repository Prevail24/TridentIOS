from pathlib import Path

from core.parsers.nmap.xml_parser import NmapXMLParser
from core.services.nmap_observation_translator import NmapObservationTranslator


parser = NmapXMLParser()
translator = NmapObservationTranslator()

xml = Path("knowledge/evidence/nmap/RUN-2026-0002.xml")

observations = parser.parse(xml)
translated = translator.translate_many(observations)

print(f"\nTranslated {len(translated)} observations\n")

for item in translated:
    print(f"- {item}")