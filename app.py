import os

from flask import Flask, request, jsonify, render_template, abort
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB("payloads.json")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/payload", methods=["POST"])
def receive_payload():
    if not request.is_json:
        abort(400, description="Request must be JSON")
    payload = request.get_json()
    doc_id = db.insert({"payload": payload})
    return jsonify({"status": "stored", "id": doc_id}), 201


@app.route("/api/payloads", methods=["GET"])
def list_payloads():
    records = db.all()
    result = []
    for record in records:
        result.append({"id": record.doc_id, "payload": record["payload"]})
    return jsonify(result)


@app.route("/api/purge", methods=["DELETE"])
def purge_payloads():
    db.truncate()
    return jsonify({"status": "purged"})


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug)
