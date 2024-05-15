import json
import tomllib

def load_file(file):
    with open(f"./data/{file}.json", "r") as f:
        return json.load(f)

def post_file(data, file):
    with open(f"./data/{file}.json", "w") as f:
        json.dump(data, f, indent=4)

def load_settings():
    with open("./data/settings.toml", "rb") as f:
        return tomllib.load(f)

def make_settings():
    with open("./data/settings.toml", "w") as f:
        f.write("minimumTickets = 0\nticketsPerRaffle = 10\n\n day = 1\ndayOneMax = 10\ndayTwoMax = 3\ndayThreeMax = 0\ndayFourMax = 0")

def total_points(temp:dict, key:str):
    total:int = 0
    print(temp)
    person = temp[key]
    total += person["dayOne"]
    total += person["dayTwo"]
    total += person["dayThree"]
    total += person["dayFour"]
    total += person["bonusOne"]
    total += person["bonusTwo"]
    total += person["bonusThree"]
    total += person["bonusFour"]
    return total


def order(person:dict):
    reordered_list = {}
    keys = list(person.keys())
    for i in range(len(person)):
        biggest_key = keys[0]
        for key in keys:
            if total_points(person, biggest_key) < total_points(person, key):
                biggest_key = key
        reordered_list[biggest_key] = total_points(person, biggest_key)
        keys.remove(biggest_key)
    return reordered_list
