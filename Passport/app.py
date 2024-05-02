from flask import Flask, render_template, request  # type: ignore
import data
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
    return render_template("home.html")

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
        elif not name in cache:
            cache[name] = 0
            data.post_file(cache, "cache")
    
    return render_template("accounts.html", cache=data.order(cache))

@app.route("/e/add", methods=["GET", "POST"])
def add():
    cache = data.load_file("cache")

    if request.method == "POST":
        name = request.form["name"]
        worth = request.form["worth"]
        if name in cache:
            cache[name] += int(worth)
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
        if cache[keys[i]] >= minimumTickets:
            raffle_tickets = math.floor((cache[keys[i]] - minimumTickets) / ticketsPerRaffle) + 1
            updated_cache[keys[i]] = raffle_tickets

    return render_template("raffle.html", cache=updated_cache)

if __name__ == "__main__":
    app.run("localhost", 8000, debug=True)