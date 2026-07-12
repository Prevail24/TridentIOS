from enum import StrEnum


class EntityType(StrEnum):
    HOST = "host"
    PORT = "port"
    SERVICE = "service"
    PRODUCT = "product"
    VERSION = "version"
    DOMAIN = "domain"
    IP = "ip"