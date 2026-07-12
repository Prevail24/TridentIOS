from datetime import date

from core.models.evidence import Evidence


class EvidenceParser:
    """
    Converts Evidence markdown into an Evidence object.
    """

    def parse(self, markdown: str) -> Evidence:
        lines = markdown.splitlines()

        title = lines[0].replace("# ", "").strip()

        metadata = {}
        notes = []

        in_notes = False

        for line in lines:
            if line.strip() == "# Notes":
                in_notes = True
                continue

            if line.startswith("# ") and line.strip() != "# Notes":
                in_notes = False

            if line.startswith("- "):
                item = line[2:].strip()

                if in_notes:
                    notes.append(item)
                    continue

                if ":" not in item:
                    continue

                key, value = item.split(":", 1)
                metadata[key.strip()] = value.strip()

        return Evidence(
            id=metadata["ID"],
            title=title,
            evidence_type=metadata["Evidence Type"],
            source=metadata["Source"],
            observation_id=metadata["Observation"],
            author=metadata["Author"],
            created=date.today(),
            updated=date.today(),
            status=metadata["Status"],
            notes=notes,
        )