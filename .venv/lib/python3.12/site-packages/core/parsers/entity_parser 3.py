from core.models.entity import Entity


class EntityParser:
    """
    Converts Entity markdown into an Entity object and back.
    """

    def parse(self, markdown: str) -> Entity:
        lines = markdown.splitlines()

        metadata = {}
        observations = []
        evidence = []
        tags = []

        current_section = None

        for line in lines:
            stripped = line.strip()

            if stripped == "# Observations":
                current_section = "observations"
                continue

            if stripped == "# Evidence":
                current_section = "evidence"
                continue

            if stripped == "# Tags":
                current_section = "tags"
                continue

            if stripped.startswith("# "):
                current_section = None
                continue

            if not stripped.startswith("- "):
                continue

            item = stripped[2:].strip()

            if current_section == "observations":
                observations.append(item)
                continue

            if current_section == "evidence":
                evidence.append(item)
                continue

            if current_section == "tags":
                tags.append(item)
                continue

            if ":" not in item:
                continue

            key, value = item.split(":", 1)
            metadata[key.strip()] = value.strip()

        return Entity(
            id=metadata["ID"],
            entity_type=metadata["Type"],
            value=metadata["Value"],
            confidence=float(metadata.get("Confidence", 1.0)),
            status=metadata.get("Status", "active"),
            observations=observations,
            evidence=evidence,
            tags=tags,
        )

    def serialize(self, entity: Entity) -> str:
        observations = "\n".join(f"- {item}" for item in entity.observations)
        evidence = "\n".join(f"- {item}" for item in entity.evidence)
        tags = "\n".join(f"- {item}" for item in entity.tags)

        return f"""# {entity.id}

## Metadata

- ID: {entity.id}
- Type: {entity.entity_type}
- Value: {entity.value}
- Confidence: {entity.confidence}
- Status: {entity.status}

---

# Observations

{observations}

---

# Evidence

{evidence}

---

# Tags

{tags}
"""