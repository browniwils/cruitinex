#!/bin/usr/python3
"""Module for handling users API endpoints."""
from api.v1 import app_views
from flask import request as req
from flask import jsonify
from flask import abort
from model.user import User
from utils.endpoint import get_model
from storage import db_engine


@app_views.route("/users")
def get_users():
    """Route for getting users."""
    users = get_model(User)
    return jsonify(users), 200


@app_views.route("/users/<user_id>")
def get_user(user_id):
    """Retrieve an user with id."""
    user = db_engine.query(User.__name__, id=user_id)
    if user:
        user = user(**user[0])
        return jsonify(user.view()), 200
    abort(404)


@app_views.route("/users", methods=["POST"])
def create_user():
    body = req.get_json()
    if body:
        username = body.get("username", None)
        password = body.get("password", None)
        first_name = body.get("first_name", None)
        last_name = body.get("last_name", None)
        email = body.get("email", None)
        role = body.get("role", None)
        new_user = User(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role,
        )
        results = db_engine.new(new_user)
        return jsonify(results), 201
    abort(400)

@app_views.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    body = req.get_json()
    if body:
        user = db_engine.query("user", id=user_id)
        user = user[0]
        for key, val in body.items():
            if key and key != "id":
                user.update({key: val})
        results = db_engine.update(**user)
        return jsonify({
            "message": "resource updated",
            "id": results.get("id", None)
        }), 204
    abort(404)

@app_views.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = db_engine.delete(user_id)
    if user:
        return jsonify(operation="successful"), 204
    abort(404)
