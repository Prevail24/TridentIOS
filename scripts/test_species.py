from core.species.registry import SpeciesRegistry


def main() -> None:
    registry = SpeciesRegistry()
    web = registry.get("web")

    web.awaken()

    for serpent in web.serpents():
        serpent.awaken()


if __name__ == "__main__":
    main()