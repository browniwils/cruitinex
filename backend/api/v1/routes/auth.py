#!/bin/usr/python3
"""Module for handling login API endpoints."""
import hashlib
from api.v1 import app_views
from base64 import b64encode
from datetime import datetime
from datetime import timedelta
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
    user = db_engine.query(User).filter_by(username=username).first()
    if not user:
        abort(404)
    hashed_password = user.hash_password(password)
    if user.password != hashed_password:
        abort(404)
    token = str(uuid4())
    session_created_at = datetime.now()
    session_expires_at = session_created_at + timedelta(minutes=30)
    session_token = {
        "email": user.email,
        "session_token": token,
        "session_created_at": session_created_at.isoformat(),
        "session_expires_at": session_expires_at.isoformat(),
        }
    encoded_session_token = b64encode(session_token.encode())
    user.session_token = session_token
    db_engine.save()
    response = jsonify({"data": user.view(), "message": "success"}), 200
    response.set_cookie("session_id", encoded_session_token.decode())
    return response

@app_views.route("/users/logout", methods=["DELETE"])
def logout():
    """Log user out."""
    session_token = req.cookies.get("session_id")
    user = db_engine.query(User).filter_by(session_token=session_token)
    user.session_token = None
    db_engine.save()
    response = jsonify({"message": "success"}), 200
    response.set_cookie("session_id", "")
    return response
