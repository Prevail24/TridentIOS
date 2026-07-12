from datetime import date

from core.models.evidence import Evidence
from core.repositories.evidence_repository import EvidenceRepository
from core.results.create_evidence_result import CreateEvidenceResult
from core.services.evidence_id_generator import EvidenceIDGenerator
from core.services.observation_service import ObservationService


class EvidenceService:
    """
    Business logic for Evidence.
    """

    def __init__(self):
        self.repository = EvidenceRepository()
        self.id_generator = EvidenceIDGenerator()

    def create(
        self,
        title: str,
        evidence_type: str,
        source: str,
        observation_id: str,
        author: str = "Prevail",
    ) -> CreateEvidenceResult:
        evidence_id = self.id_generator.generate()

        evidence = Evidence(
            id=evidence_id,
            title=title,
            evidence_type=evidence_type,
            source=source,
            observation_id=observation_id,
            author=author,
            created=date.today(),
            updated=date.today(),
        )

        filepath = self.repository.save(evidence)

        ObservationService().add_evidence(
            observation_id=observation_id,
            evidence_id=evidence.id,
        )

        return CreateEvidenceResult(
            evidence=evidence,
            filepath=str(filepath),
        )

    def count(self) -> int:
        """
        Return the total number of Evidence objects stored in The Loom.
        """
        return len(self.repository.list())