from flask import Flask, render_template, request  # type: ignore
import uuid
import json
import data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/e/accounts", methods=["GET", "POST"])
def accounts():
    cache = data.load_file("cache")

    if request.method == "POST":
        name = request.form["name"]
        cache[name] = 0
        data.post_file(cache, "cache")
    
    return render_template("accounts.html", cache=cache)

@app.route("/e/add", methods=["GET", "POST"])
def add():
    cache = data.load_file("cache")

    if request.method == "POST":
        name = request.form["name"]
        worth = request.form["worth"]

        cache[name] += int(worth)
        data.post_file(cache, "cache")

    return render_template("add.html")

if __name__ == "__main__":
    app.run("localhost", 8000, debug=True)