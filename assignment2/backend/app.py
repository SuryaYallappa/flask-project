import os

import pymongo
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, request

load_dotenv()

mongo_url = os.getenv("mongo_url")
print(mongo_url)
client = pymongo.MongoClient(mongo_url)
db = client.test

collection = db["test_collection"]

app = Flask(__name__)


@app.route("/submit", methods=["POST"])
def submit():
    name = request.json
    try:
        collection.insert_one(name)
        return redirect("/success")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/view")
def view():
    data = list(collection.find())
    for item in data:
        del item["_id"]
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000,debug=True)
