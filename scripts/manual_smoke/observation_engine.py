from core.repositories.observation_repository import ObservationRepository
from core.services.observation_engine import ObservationEngine


repo = ObservationRepository()
engine = ObservationEngine()

observation = repo.list()[-1]

result = engine.process(observation)
entities = result["entities"]
relationships = result["relationships"]

print()
print("Observation Processed")
print("---------------------")
print(f"Observation: {observation.id}")
print(f"Category: {observation.category}")
print()

for entity in entities:
    print(f"{entity.id} | {entity.entity_type} | {entity.value}")

print()
print("Relationships")
print("-------------")

for relationship in relationships:
    print(
        f"{relationship.id} | "
        f"{relationship.source_id} "
        f"{relationship.relationship_type} "
        f"{relationship.target_id}"
    )