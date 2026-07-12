from pathlib import Path
from datetime import date
import shutil

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "OBSERVATION_TEMPLATE.md"
OBS_ROOT = ROOT / "knowledge" / "observations"


def next_observation_id(year: int):
    year_dir = OBS_ROOT / str(year)
    year_dir.mkdir(parents=True, exist_ok=True)

    existing = sorted(year_dir.glob("OBS-*.md"))

    if not existing:
        number = 1
    else:
        last = existing[-1].stem
        number = int(last.split("-")[-1]) + 1

    return f"OBS-{year}-{number:04d}", year_dir


def create_observation(title, platform, category, difficulty):
    today = date.today()
    year = today.year

    obs_id, year_dir = next_observation_id(year)
    destination = year_dir / f"{obs_id}.md"

    shutil.copy(TEMPLATE, destination)
    text = destination.read_text(encoding="utf-8")

    replacements = {
        "OBS-YYYY-0001": obs_id,
        'title: ""': f'title: "{title}"',
        'platform: ""': f'platform: "{platform}"',
        'category: ""': f'category: "{category}"',
        'difficulty: ""': f'difficulty: "{difficulty}"',
        'created: YYYY-MM-DD': f'created: {today.isoformat()}',
        'updated: YYYY-MM-DD': f'updated: {today.isoformat()}',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    destination.write_text(text, encoding="utf-8")

    return obs_id, destination