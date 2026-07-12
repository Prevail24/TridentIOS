from core.models.graph import GraphNode
from core.services.mission_service import MissionService
from core.services.observation_service import ObservationService


class Cartographer:
    """
    Builds graph representations of investigations.
    """
    
    def __init__(self):
        self.missions = MissionService()
        self.observations = ObservationService()

    def map_mission(self, mission_id: str) -> GraphNode:
        """
        Build a graph from a Mission.
        """

        mission = self.missions.open(mission_id)

        root = GraphNode(
            id=mission.id,
            label=mission.title,
        )

        for observation_id in mission.observations:

            observation = self.observations.open(observation_id)

            observation_node = GraphNode(
                id=observation.id,
                label=observation.id,
            )

            for evidence_id in observation.evidence:

                evidence_node = GraphNode(
                    id=evidence_id,
                    label=evidence_id,
                )

                observation_node.children.append(evidence_node)

            root.children.append(observation_node)

        return root