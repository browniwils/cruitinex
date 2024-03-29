#!/bin/usr/python3
"""Module for handling users API endpoints."""
from api.v1 import app_views
from model.user import User
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/users")
@authentication_required
@authorization_required(AUTH.READ)
def get_users():
    """Retrieve all user and paginate."""
    return get_all(User)


@app_views.route("/users/<user_id>")
@authentication_required
@authorization_required(AUTH.READ)
def get_user(user_id):
    """Retrieve user with user's id from model table."""
    return get_one(User, user_id)


@app_views.route("/users", methods=["POST"])
def create_user():
    """Create user record in model table."""
    return create_entry(User)

@app_views.route("/users/<user_id>", methods=["PUT"])
@authentication_required
@authorization_required(AUTH.UPDATE)
def update_user(user_id):
    """Update user record in model table."""
    return update_entry(User, user_id)

@app_views.route("/users/<user_id>", methods=["DELETE"])
@authentication_required
@authorization_required(AUTH.DELETE)
def delete_user(user_id):
    """Delete user record in model table."""
    return delete_entry(User, user_id)
