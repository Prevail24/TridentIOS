from core.engine import TridentEngine
from core.renderers.relationship_renderer import RelationshipRenderer

def create_relationship():
    engine = TridentEngine()

    print()

    source = input("Source Entity : ")
    relationship = input("Relationship  : ")
    target = input("Target Entity : ")

    result = engine.relationships.create(
        source=source,
        relationship=relationship,
        target=target,
    )

    print()
    print("✓ Relationship created")
    print(f"ID           : {result.id}")
    print(f"Source       : {result.source}")
    print(f"Relationship : {result.relationship}")
    print(f"Target       : {result.target}")
    print()

def open_relationship(relationship_id: str):

    engine = TridentEngine()

    relationship = engine.relationships.open(
        relationship_id
    )

    RelationshipRenderer().render(
        relationship
    )