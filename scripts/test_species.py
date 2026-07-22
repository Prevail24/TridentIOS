from core.species.registry import SpeciesRegistry


registry = SpeciesRegistry()

web = registry.get("web")

web.awaken()

for serpent in web.serpents():

    serpent.awaken()

    for capability in serpent.capabilities():

        capability.awaken()

        for weapon in capability.weapons():

            weapon.awaken()