import requests
from flask import Flask, render_template, request

BACKEND_URL = "https://todo-app-7l07.onrender.com"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    from_data = dict(request.form)

    requests.post(f"{BACKEND_URL}/submittodoitem", json=from_data)
    return "Data submitted successfully!"


@app.route("/view")
def view():
    response = requests.get(f"{BACKEND_URL}/view")
    return response.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
