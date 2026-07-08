from core.intelligence.entity import Entity


class EntityEngine:
    """
    Correlates observations into canonical entities.
    """

    def __init__(self):
        self.entities = {}

    def get_or_create(self, entity_type, value):

        key = (entity_type, value)

        if key not in self.entities:
            self.entities[key] = Entity(entity_type, value)

        return self.entities[key]

    def add_observation(self, entity_type, value, observation):

        entity = self.get_or_create(entity_type, value)

        entity.add_observation(observation)

        return entity