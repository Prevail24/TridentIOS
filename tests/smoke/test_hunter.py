from core.serpents.hunter import Hunter

hunter = Hunter()

print()
print("HUNTER")
print("------")

recommendations = hunter.hunt("45.33.32.156")

if not recommendations:
    print("No recommendations.")
else:
    for recommendation in recommendations:
        print("-", recommendation)