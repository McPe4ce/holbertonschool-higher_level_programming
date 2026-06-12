#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    JWTManager,
    get_jwt,
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-please-change-me-1234"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"},
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
          check_password_hash(users[username]["password"], password):
        return username


@app.route('/')
@auth.login_required
def greetings():
    return f"Hello there, {auth.current_user}"


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username not in users or \
            not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    additional_claims = {"role": users[username]["role"]}
    access_token = create_access_token(identity=username,
                                       additional_claims=additional_claims)
    return jsonify(access_token=access_token)


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic():
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(port=5000)
