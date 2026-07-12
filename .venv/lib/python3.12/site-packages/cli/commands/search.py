from core.services.search_service import SearchService
from core.renderers.entity_renderer import EntityRenderer


def search(query: str):

    service = SearchService()

    matches = service.entities_by_value(query)

    print()

    print("🔎 SEARCH RESULTS")

    print()

    if not matches:

        print("No matches found.")
        print()

        return

    renderer = EntityRenderer()

    for entity in matches:

        renderer.render(entity)