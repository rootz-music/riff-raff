# Save/load/export lyrics/hooks

import json

def save_lyrics(lyrics, file_path="data/saved_lyrics.json"):
    with open(file_path, "w") as f:
        json.dump(lyrics, f)

def load_lyrics(file_path="data/saved_lyrics.json"):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
