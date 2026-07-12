from enum import StrEnum


class RelationshipType(StrEnum):
    HAS_PORT = "HAS_PORT"
    RUNS_SERVICE = "RUNS_SERVICE"
    HAS_PRODUCT = "HAS_PRODUCT"
    HAS_VERSION = "HAS_VERSION"
    RESOLVES_TO = "RESOLVES_TO"