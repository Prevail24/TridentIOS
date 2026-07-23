from core.serpents.hunter import Hunter


hunter = Hunter()

leads = hunter.hunt("45.33.32.156")

print()
print("HUNTER")
print("------")

if not leads:
    print("No investigative leads identified.")
else:
    for lead in leads:
        print(f"- {lead}")