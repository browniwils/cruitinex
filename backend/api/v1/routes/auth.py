#!/bin/usr/python3
"""Module for handling login API endpoints."""
from api.v1 import app_views
from flask import abort
from flask import jsonify
from flask import request as req
from model.user import User
from storage import db_engine
from uuid import uuid4


@app_views.route("/users/login", methods=["POST"])
def login():
    """Log user in."""
    body = req.get_json()
    if not body.get("username", None) or not body.get("password", None):
        abort(400)

    username = body.get("username")
    password = body.get("password")
    user = db_engine.query(User).filter_by(username=username, password=password).first()
    if not user:
        abort(404)
    session_token = str(uuid4())
    user.session_token = session_token
    db_engine.save()
    response = jsonify({"data": user.view(), "message": "success"}), 200
    response.set_cookie("session_token", session_token)
    return response

@app_views.route("/users/logout")
def logout():
    """Log user out."""
    session_token = req.cookies.get("session_token")
    user = db_engine.query(User).filter_by(session_token=session_token)
    user.session_token = None
    db_engine.save()
    return jsonify({"message": "success"}), 200

