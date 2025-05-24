from flask import Flask, render_template, redirect, request, session, url_for
import random
import time

app = Flask(__name__)
app.secret_key = "eggsaresodelicious"

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True, port=8000)