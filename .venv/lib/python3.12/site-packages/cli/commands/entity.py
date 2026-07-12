from core.engine import TridentEngine
from core.renderers.entity_renderer import EntityRenderer

engine = TridentEngine()


def create_entity():

    print()

    entity_type = input("Entity Type  : ")
    value = input("Entity Value : ")

    print()

    entity = engine.entity.create(
        type=entity_type,
        value=value,
    )

    print("✓ Entity created")

    print(f"ID    : {entity.id}")
    print(f"Type  : {entity.type}")
    print(f"Value : {entity.value}")

    print()


def open_entity(entity_id: str):
    entity = engine.entity.open(entity_id)
    EntityRenderer().render(entity)