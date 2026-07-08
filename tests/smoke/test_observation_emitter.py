from core.services.observation_emitter import ObservationEmitter


emitter = ObservationEmitter()

observation = emitter.emit(
    mission_id="MIS-2026-0001",
    tool_run_id="RUN-2026-0002",
    evidence_id="RUN-2026-0002.xml",
    category="port",
    data={
        "host": "45.33.32.156",
        "port": 22,
        "protocol": "tcp",
        "state": "open",
        "service": "ssh",
    },
)

print()
print("Observation Created")
print("-------------------")
print(observation.id)
print(observation.category)
print(observation.data)
print()