import json

def load_file(file):
    with open(f"./data/{file}.json", "r") as f:
        return json.load(f)