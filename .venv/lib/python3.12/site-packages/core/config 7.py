from pathlib import Path


class Config:
    APP_NAME = "TridentIOS"
    VERSION = "0.5.0-alpha"

    OBSERVER_NAME = "Prevail"

    ROOT_DIR = Path(__file__).resolve().parent.parent
    KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
    OBSERVATIONS_DIR = KNOWLEDGE_DIR / "observations"
    LOGS_DIR = ROOT_DIR / "logs"

    BRAND_QUOTE = "The Loom remembers what others forget."