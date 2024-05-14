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

def make_settings():
    with open(f"./data/settings.toml", "w") as f:
        f.write("minimumTickets = 0\nticketsPerRaffle = 10\n\n day = 1\ndayOneMax = 10\ndayTwoMax = 3\ndayThreeMax = 0\ndayFourMax = 0")

def order(dict):
    reordered_list = {}
    keys = list(dict.keys())
    for i in range(len(dict)):
        biggest_key = keys[0]
        for key in keys:
            if dict[biggest_key] < dict[key]:
                biggest_key = key
        reordered_list[biggest_key] = dict[biggest_key]
        keys.remove(biggest_key)
    return reordered_list
