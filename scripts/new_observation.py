from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.observation_manager import create_observation


def main():
    title = input("Observation Title: ").strip()
    platform = input("Platform (HTB, THM, PicoCTF, etc.): ").strip()
    category = input("Category: ").strip()
    difficulty = input("Difficulty: ").strip()

    obs_id, destination = create_observation(
        title=title,
        platform=platform,
        category=category,
        difficulty=difficulty,
    )

    print("\nObservation created successfully!")
    print(f"ID:   {obs_id}")
    print(f"File: {destination}")


if __name__ == "__main__":
    main()