from flask import Flask, json, request, jsonify

app = Flask(__name__)


@app.route("/api")
def api():
    with open("sample.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
