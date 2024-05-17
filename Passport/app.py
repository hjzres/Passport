from flask import Flask, render_template, request  # type: ignore
from . import data
import pathlib
import math

app = Flask(__name__)

data_folder = pathlib.Path("./data/")
data_folder.mkdir(exist_ok=True, parents=True)
if not (data_folder / "cache.json").is_file():
    data.post_file({}, "cache")
if not (data_folder / "deleted.json").is_file():
    data.post_file({}, "deleted")
if not (data_folder / "settings.toml").is_file():
    data.make_settings()

@app.route("/")
def home():
    settings = data.load_settings()
    day = settings["day"]
    return render_template("home.html", day=day)

@app.route("/e/accounts", methods=["GET", "POST"])
def accounts():
    cache = data.load_file("cache")

    if request.method == "POST":
        name = request.form["name"] 
        if request.form.get('_method') == 'PUT':
            deleted = data.load_file("deleted")
            deleted[name] = cache[name]
            del cache[name]
            data.post_file(deleted, "deleted")
            data.post_file(cache, "cache")
        elif name not in cache:
            cache[name] = {
                "dayOne": 0,
                "dayTwo": 0,
                "dayThree": 0,
                "dayFour": 0,
                "bonusOne": 0,
                "bonusTwo": 0,
                "bonusThree": 0
            }
            data.post_file(cache, "cache")
    
    return render_template("accounts.html", cache=data.order(cache))

@app.route("/e/add", methods=["GET", "POST"])
def add():
    cache = data.load_file("cache")
    setting = data.load_settings()

    if request.method == "POST":
        name = request.form["name"]
        worth = request.form["worth"]
        if name in cache:
            match setting['day']:
                case 1:
                    if cache[name]['dayOne'] + int(worth) <= setting['dayOneMax']:
                        cache[name]['dayOne'] += int(worth)
                        if cache[name]['dayOne'] == setting['dayOneMax'] and cache[name]['bonusOne'] != 5:
                            cache[name]['bonusOne'] = 5
                case 2:
                    if cache[name]['dayTwo'] + int(worth) <= setting['dayTwoMax']:
                        cache[name]['dayTwo'] += int(worth)
                        if cache[name]['dayTwo'] == setting['dayTwoMax'] and cache[name]['bonusTwo'] != 5:
                            cache[name]['bonusTwo'] = 5
                case 3:
                    if cache[name]['dayThree'] + int(worth) <= setting['dayThreeMax']:
                        cache[name]['dayThree'] += int(worth)
                        if cache[name]['dayThree'] == setting['dayThreeMax'] and cache[name]['bonusThree'] != 5:
                            cache[name]['bonusThree'] = 5
                case 4:
                    if cache[name]['dayFour'] + int(worth) <= setting['dayFourMax']:
                        cache[name]['dayFour'] += int(worth)
            
            data.post_file(cache, "cache")
        else:
            return render_template("add.html", error="That name is not in the system")

    return render_template("add.html")

@app.route("/e/raffle")
def raffle():
    cache = data.load_file("cache")
    updated_cache = {}
    keys = list(cache.keys())
    settings = data.load_settings()
    minimumTickets = settings["minimumTickets"]
    ticketsPerRaffle = settings["ticketsPerRaffle"] 
    for i in range(len(keys)):
        print(data.total_points(cache, keys[i]))
        print(cache[keys[i]])
        if data.total_points(cache, keys[i]) >= minimumTickets:
            raffle_tickets = math.floor((data.total_points(cache, keys[i]) - minimumTickets) / ticketsPerRaffle) + 1
            updated_cache[keys[i]] = raffle_tickets

    return render_template("raffle.html", cache=updated_cache)

if __name__ == "__main__":
    app.run("localhost", 8000, debug=True)