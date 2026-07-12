from core.ui.dossier import Dossier


class EntityRenderer:

    def render(self, entity):

        dossier = Dossier(
            title=entity.id,
            subtitle="Entity Intelligence",
            color="magenta",
            icon="🟣",
        )

        dossier.add("Type", entity.type)
        dossier.add("Value", entity.value)
        dossier.add("Confidence", entity.confidence)
        dossier.add("Status", entity.status.upper())

        dossier.render()