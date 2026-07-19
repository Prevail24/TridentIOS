from core.species.registry import SpeciesRegistry


def main():
    registry = SpeciesRegistry()

    for species in registry.all():
        species.awaken()


if __name__ == "__main__":
    main()