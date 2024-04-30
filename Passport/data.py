import json
import tomllib

def load_file(file):
    with open(f"./data/{file}.json", "r") as f:
        return json.load(f)

def post_file(data, file):
    with open(f"./data/{file}.json", "w") as f:
        json.dump(data, f, indent=4)

def load_settings():
    with open(f"./data/settings.toml", "rb") as f:
        return tomllib.load(f)