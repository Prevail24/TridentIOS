from core.services.diff_engine import DiffEngine


engine = DiffEngine()

result = engine.compare("45.33.32.156")

if result is None:
    print("Entity not found")
    raise SystemExit(1)

print()
print("DIFF ENGINE")
print("-----------")
print(result["entity"].value)

for relationship_type, targets in result["graph"].items():
    print()
    print(relationship_type)

    for target in targets:
        print(f"  {target.entity_type}: {target.value}")