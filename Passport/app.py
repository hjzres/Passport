from flask import Flask, render_template  # type: ignore
import uuid
import json
import data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/accounts")
def accounts():
    return render_template("accounts.html")

@app.route("/add")
def add():
    return render_template("add.html")