from core.services.loom_service import LoomService


def render_tree(loom, entity, prefix=""):
    relationships = loom.outgoing_relationships(entity.id)

    for relationship, target in relationships:
        print(f"{prefix}└── {relationship.relationship_type}")
        print(f"{prefix}    └── {target.entity_type}: {target.value}")

        render_tree(
            loom,
            target,
            prefix + "        ",
        )

def show_loom(entity_value: str):
    loom = LoomService()

    result = loom.graph_for_entity(entity_value)

    if result is None:
        print("Entity not found.")
        return

    entity, graph = result

    print()
    print("═══════════════════════════════")
    print("          THE LOOM")
    print("═══════════════════════════════")
    print()

    print(f"{entity.entity_type.upper()}")
    print(f"{entity.value}")
    print()

    if not graph:
        print("No relationships.")
        return

    render_tree(loom, entity)