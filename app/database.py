import json
from pathlib import Path


DATA_FILE = Path(__file__).parent.parent / "data" / "shoots.json"


def load_shoots():
    """Load shoot records from JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_shoots(shoots):
    """Save shoot records to JSON file."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(shoots, file, indent=4)