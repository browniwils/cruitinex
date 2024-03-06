#!/bin/usr/python3
"""Module for handling login API endpoints."""
from api.v1 import app_views
from datetime import datetime
from datetime import timedelta
from flask import abort
from flask import jsonify
from flask import request as req
from model.user import User
from storage import db_engine
from uuid import uuid4


@app_views.route("/login", methods=["POST"])
def login():
    """Log user in."""
    body = req.get_json()
    if not body.get("username", None) or not body.get("password", None):
        abort(400)

    username = body.get("username")
    password = body.get("password")
    user = db_engine.query(User).filter_by(username=username).first()
    if not user:
        abort(404)
    hashed_password = user.hash_password(password)
    if user.password != hashed_password:
        abort(404)
    sesstion_token = str(uuid4())
    user.updated_at = datetime.now()
    user.session_token = sesstion_token
    db_engine.save()
    response = jsonify(message="successful login")
    response.set_cookie("session_id", user.session_token,
                        expires=user.updated_at + timedelta(days=3))
    return response, 200

@app_views.route("/logout", methods=["DELETE"])
def logout():
    """Log user out."""
    session_token = req.cookies.get("session_id")
    if session_token:
        user = db_engine.query(User).filter_by(
            session_token=session_token).first()
        if user:
            user.session_token = None
            user.updated_at = datetime.now()
            db_engine.save()
    response = jsonify({"message": "success"}), 200
    response.set_cookie("session_id", None)
    return response
