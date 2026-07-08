from core.services.entity_resolver import EntityResolver
from core.services.relationship_engine import RelationshipEngine


class ObservationEngine:
    """
    Converts canonical observations into entities and relationships.
    """

    def __init__(self):
        self.entities = EntityResolver()
        self.relationships = RelationshipEngine()

    def process(self, observation):
        resolved = []
        relationships = []

        if observation.category == "port":
            host = self.entities.resolve(
                "host",
                observation.data["host"],
            )

            port = self.entities.resolve(
                "port",
                f'{observation.data["protocol"]}/{observation.data["port"]}',
            )

            service = self.entities.resolve(
                "service",
                observation.data.get("service", "unknown"),
            )

            product = None
            version = None

            if observation.data.get("product"):
                product = self.entities.resolve(
                    "product",
                    observation.data["product"],
                )

            if observation.data.get("version"):
                version = self.entities.resolve(
                    "version",
                    observation.data["version"],
                )

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

        return {
            "entities": resolved,
            "relationships": relationships,
        }