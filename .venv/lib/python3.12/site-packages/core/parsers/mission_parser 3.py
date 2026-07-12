from datetime import date

from core.models.mission import Mission


class MissionParser:
    """
    Converts Mission markdown into a Mission object.
    """

    def parse(self, markdown: str) -> Mission:
        lines = markdown.splitlines()

        title = lines[0].replace("# ", "").strip()

        metadata = {}
        observations = []
        in_observations = False

        for line in lines:
            if line.strip() == "# Observations":
                in_observations = True
                continue

            if line.startswith("# ") and line.strip() != "# Observations":
                in_observations = False

            if line.startswith("- "):
                item = line[2:].strip()

                if in_observations:
                    observations.append(item)
                    continue

                if ":" not in item:
                    continue

                key, value = item.split(":", 1)
                metadata[key.strip()] = value.strip()

        return Mission(
            id=metadata["ID"],
            title=title,
            mission_type=metadata["Mission Type"],
            priority=metadata["Priority"],
            observer=metadata["Observer"],
            created=date.today(),
            updated=date.today(),
            status=metadata["Status"],
            observations=observations,
        )