#!/usr/bin/python3

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return b"Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return b"OK"


@app.errorhandler(404)
def error_404(error=None):
    return jsonify({"error": "User not found"}), 404


@app.errorhandler(400)
def error_400(error=None):
    return jsonify({"error": error.description}), 400


@app.errorhandler(409)
def error_409(error=None):
    return jsonify({"error": "Username already exists"}), 409


@app.route("/users/<username>")
def user(username):
    if username not in users:
        return error_404()
    else:
        return jsonify(users[username])


@app.route("/add_user", methods=['POST'])
def add_user():
    new_user = request.get_json(silent=True)

    if new_user is None:
        abort(400, description="Invalid JSON")

    username = new_user.get("username")

    if not username:
        abort(400, description="Username is required")

    if username in users:
        abort(409, description="")
    users[username] = new_user
    return jsonify(new_user), 201


if __name__ == "__main__":
    app.run()
