from core.services.entity_service import EntityService


class SearchService:
    """
    Search The Loom.
    """

    def __init__(self):
        self.entities = EntityService()

    def entities_by_value(self, query: str):

        query = query.lower()

        matches = []

        for entity in self.entities.list():

            if query in entity.value.lower():
                matches.append(entity)

        return matches