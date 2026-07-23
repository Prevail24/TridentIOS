from core.services.loom_service import LoomService


loom = LoomService()

result = loom.graph_for_entity("45.33.32.156")

if result is None:
    print("Entity not found")
    raise SystemExit(1)

entity, graph = result

print()
print("THE LOOM")
print("--------")
print(f"{entity.entity_type}: {entity.value}")
print()

for relationship_type, targets in graph.items():
    print(relationship_type)

    for target in targets:
        if target is None:
            continue

        print(f"  -> {target.entity_type}: {target.value}")

print()
