from datetime import datetime

import requests
from flask import Flask, render_template, request

BACKEND_URL = "http://127.0.0.1:9000"
app = Flask(__name__)


@app.route("/")
def home():
    day_of_week = datetime.now().strftime("%A")
    return render_template("index.html", day_of_week=day_of_week)


@app.route("/submit", methods=["POST"])
def submit():
    from_data = dict(request.form)

    requests.post(f"{BACKEND_URL}/submit", json=from_data)

    return "Data submitted successfully!"

@app.route("/view")
def view():
    response = requests.get(f"{BACKEND_URL}/view")
   
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
