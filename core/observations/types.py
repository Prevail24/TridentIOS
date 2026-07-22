from enum import StrEnum


class ObservationType(StrEnum):
    IP_ADDRESS = "ip_address"
    HOSTNAME = "hostname"
    PORT = "port"
    HTTP_SERVICE = "http_service"
    REDIRECT = "redirect"
    TECHNOLOGY = "technology"
    VIRTUAL_HOST = "virtual_host"
    DIRECTORY = "directory"