from core.serpents.oracle import Oracle

oracle = Oracle()

print()
print("ORACLE")
print("------")

for h in oracle.hypothesize("45.33.32.156"):

    print(
        f"[{h['confidence'].upper()}] "
        f"{h['hypothesis']}"
    )