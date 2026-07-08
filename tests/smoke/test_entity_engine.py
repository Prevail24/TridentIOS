from core.intelligence.entity_engine import EntityEngine


engine = EntityEngine()

engine.add_observation(
    "host",
    "45.33.32.156",
    {"sensor": "nmap"},
)

engine.add_observation(
    "host",
    "45.33.32.156",
    {"sensor": "httpx"},
)

entity = engine.get_or_create(
    "host",
    "45.33.32.156",
)

print()
print("ENTITY ENGINE")
print("-------------")
print(f"Type         : {entity.entity_type}")
print(f"Value        : {entity.value}")
print(f"Observations : {entity.observation_count}")