import os

import pymongo
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, request

load_dotenv()

mongo_url = os.getenv("mongo_url")
client = pymongo.MongoClient(mongo_url)

db = client.test
todo_collection = db["todo_items"]

app = Flask(__name__)

@app.route("/submittodoitem", methods=["POST"])
def submit():
    name = request.json
    try:
        todo_collection.insert_one(name)
        return redirect("/success")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/view")
def view():
    data = list(todo_collection.find())
    for item in data:
        del item["_id"]
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000,debug=True)
