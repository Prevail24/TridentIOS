from core.serpents.historian import Historian

historian = Historian()

timeline = historian.reconstruct("45.33.32.156")

print()
print("HISTORIAN")
print("----------")

for event in timeline:
    print(event)