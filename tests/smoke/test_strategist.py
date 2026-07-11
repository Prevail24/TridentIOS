
from core.serpents.strategist import Strategist

strategist = Strategist()

print()
print("STRATEGIST")
print("-----------")

plan = strategist.plan("45.33.32.156")

if not plan:
    print("No operational recommendations.")
else:
    for step in plan:
        print(f"- {step}")