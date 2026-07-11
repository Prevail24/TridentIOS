from core.serpents.archivist import Archivist


archivist = Archivist()

observations = archivist.retrieve("MIS-2026-0001")
print()
print("ARCHIVIST")
print("---------")
print("Observations retrieved:", len(observations))

for observation in observations:
    print(
        observation.id,
        observation.category,
        observation.observed_at,
    )