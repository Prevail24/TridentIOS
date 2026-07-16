from core.services.entity_resolver import EntityResolver
from core.services.relationship_engine import RelationshipEngine


class ObservationEngine:
    """
    Converts canonical observations into entities and relationships.
    """

    def __init__(self):
        self.entities = EntityResolver()
        self.relationships = RelationshipEngine()

    def _remember(self, entity, observation):
        entity.add_observation(observation.id)

        if observation.evidence_id:
            entity.add_evidence(observation.evidence_id)

        self.entities.repository.save(entity)

        return entity

    def process(self, observation):
        resolved = []
        relationships = []

        if observation.category == "port":
            host = self.entities.resolve(
                "host",
                observation.data["host"],
            )
            self._remember(host, observation)

            port = self.entities.resolve(
                "port",
                f'{observation.data["protocol"]}/{observation.data["port"]}',
            )
            self._remember(port, observation)

            service = self.entities.resolve(
                "service",
                observation.data.get("service", "unknown"),
            )
            self._remember(service, observation)

            product = None
            version = None

            if observation.data.get("product"):
                product = self.entities.resolve(
                    "product",
                    observation.data["product"],
                )
                self._remember(product, observation)

            if observation.data.get("version"):
                version = self.entities.resolve(
                    "version",
                    observation.data["version"],
                )
                self._remember(version, observation)

            if product:
                service_product = self.relationships.create(
                    source_id=service.id,
                    target_id=product.id,
                    relationship_type="runs_product",
                )

                relationships.append(service_product)
                resolved.append(product)

            if version:
                version_relationship = self.relationships.create(
                    source_id=product.id if product else service.id,
                    target_id=version.id,
                    relationship_type="has_version",
                )

                relationships.append(version_relationship)
                resolved.append(version)

            host_port = self.relationships.create(
                source_id=host.id,
                target_id=port.id,
                relationship_type="exposes",
            )

            port_service = self.relationships.create(
                source_id=port.id,
                target_id=service.id,
                relationship_type="runs_service",
            )

            resolved.extend([host, port, service])
            relationships.extend([
                host_port,
                port_service,
            ])

        elif observation.category == "http_endpoint":
            data = observation.data

            host = None
            url = None
            port = None

            if data.get("host"):
                host = self.entities.resolve(
                    "host",
                    data["host"],
                )
                self._remember(host, observation)
                resolved.append(host)

            if data.get("url"):
                url = self.entities.resolve(
                    "url",
                    data["url"],
                )
                self._remember(url, observation)
                resolved.append(url)

            if data.get("port") is not None:
                scheme = data.get("scheme") or "tcp"

                port = self.entities.resolve(
                    "port",
                    f"{scheme}/{data['port']}",
                )
                self._remember(port, observation)
                resolved.append(port)

            if host and port:
                relationships.append(
                    self.relationships.create(
                        source_id=host.id,
                        target_id=port.id,
                        relationship_type="exposes",
                    )
                )

            if host and url:
                relationships.append(
                    self.relationships.create(
                        source_id=host.id,
                        target_id=url.id,
                        relationship_type="exposes_url",
                    )
                )

            if port and url:
                relationships.append(
                    self.relationships.create(
                        source_id=port.id,
                        target_id=url.id,
                        relationship_type="serves_endpoint",
                    )
                )

            if url and data.get("webserver"):
                web_server = self.entities.resolve(
                    "web_server",
                    data["webserver"],
                )
                self._remember(web_server, observation)

                resolved.append(web_server)

                relationships.append(
                    self.relationships.create(
                        source_id=url.id,
                        target_id=web_server.id,
                        relationship_type="served_by",
                    )
                )

            if url:
                for technology_value in data.get("technologies", []):
                    if not technology_value:
                        continue

                    technology = self.entities.resolve(
                        "technology",
                        technology_value,
                    )
                    self._remember(technology, observation)

                    resolved.append(technology)

                    relationships.append(
                        self.relationships.create(
                            source_id=url.id,
                            target_id=technology.id,
                            relationship_type="uses_technology",
                        )
                    )

            if host:
                addresses = []

                if data.get("host_ip"):
                    addresses.append(data["host_ip"])

                addresses.extend(data.get("ipv4_addresses", []))
                addresses.extend(data.get("ipv6_addresses", []))

                for address in dict.fromkeys(addresses):
                    if not address:
                        continue

                    ip = self.entities.resolve(
                        "ip",
                        address,
                    )
                    self._remember(ip, observation)

                    resolved.append(ip)

                    relationships.append(
                        self.relationships.create(
                            source_id=host.id,
                            target_id=ip.id,
                            relationship_type="resolves_to",
                        )
                    )
            

        elif observation.category == "web_path":
            data = observation.data

            base_url = None
            discovered_url = None
            redirect_url = None

            if data.get("base_url"):
                base_url = self.entities.resolve(
                    "url",
                    data["base_url"],
                )
                self._remember(base_url, observation)
                resolved.append(base_url)

            if data.get("url"):
                discovered_url = self.entities.resolve(
                    "url",
                    data["url"],
                )
                self._remember(discovered_url, observation)
                resolved.append(discovered_url)

            if base_url and discovered_url:
                relationships.append(
                    self.relationships.create(
                        source_id=base_url.id,
                        target_id=discovered_url.id,
                        relationship_type="exposes_path",
                    )
                )

            if data.get("redirect_location"):
                redirect_url = self.entities.resolve(
                    "url",
                    data["redirect_location"],
                )
                self._remember(redirect_url, observation)
                resolved.append(redirect_url)

            if discovered_url and redirect_url:
                relationships.append(
                    self.relationships.create(
                        source_id=discovered_url.id,
                        target_id=redirect_url.id,
                        relationship_type="redirects_to",
                    )
                )

        return {
            "entities": resolved,
            "relationships": relationships,
        }