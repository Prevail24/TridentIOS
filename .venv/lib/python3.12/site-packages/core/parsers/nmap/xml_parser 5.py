import xml.etree.ElementTree as ET
from pathlib import Path

from core.models.nmap_observation import NmapObservation


class NmapXMLParser:
    """
    Parses Nmap XML into native NmapObservation objects.
    """

    def parse(self, xml_file: Path) -> list[NmapObservation]:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        observations = []

        for host in root.findall("host"):

            address = host.find("address")

            if address is None:
                continue

            ip = address.attrib.get("addr")

            ports = host.find("ports")

            if ports is None:
                continue

            for port in ports.findall("port"):

                protocol = port.attrib.get("protocol")
                portid = int(port.attrib.get("portid"))

                state = port.find("state")
                service = port.find("service")

                observations.append(
                    NmapObservation(
                        host=ip,
                        port=portid,
                        protocol=protocol,
                        state=state.attrib.get("state"),
                        service=service.attrib.get("name") if service is not None else None,
                        product=service.attrib.get("product") if service is not None else None,
                        version=service.attrib.get("version") if service is not None else None,
                        extrainfo=service.attrib.get("extrainfo") if service is not None else None,
                    )
                )

        return observations