from core.services.mission_service import MissionService
from core.services.observation_service import ObservationService
from core.services.evidence_service import EvidenceService
from core.services.entity_service import EntityService
from core.services.relationship_service import RelationshipService
from core.services.state_service import StateService
from core.services.tool_run_service import ToolRunService

class TridentEngine:
    def __init__(self):
        self.observations = ObservationService()
        self.missions = MissionService()
        self.evidence = EvidenceService()
        self.entity = EntityService()
        self.tool_runs = ToolRunService()
        self.relationships = RelationshipService()
        self.state = StateService()