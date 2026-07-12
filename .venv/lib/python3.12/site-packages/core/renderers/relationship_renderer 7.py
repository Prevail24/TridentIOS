from core.ui.dossier import Dossier


class RelationshipRenderer:
    def render(self, relationship):
        dossier = Dossier(
            title=relationship.id,
            subtitle="Relationship Intelligence",
            color="yellow",
            icon="🔗",
        )

        dossier.add("Source", relationship.source)
        dossier.add("Relationship", relationship.relationship)
        dossier.add("Target", relationship.target)
        dossier.add("Confidence", relationship.confidence)
        dossier.add("Status", relationship.status.upper())

        dossier.render()