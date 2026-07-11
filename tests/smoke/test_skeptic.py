from core.serpents.skeptic import Skeptic

skeptic = Skeptic()

print()
print("SKEPTIC")
print("--------")

results = skeptic.verify("45.33.32.156")

if not results:
    print("No hypotheses to verify.")
else:
    for result in results:
        print(
            f"[{result['status'].upper()}] "
            f"{result['hypothesis']}"
        )