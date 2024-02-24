#!/bin/usr/python3
"""Module for handling roles API endpoints."""
from api.v1 import app_views
from model.privilage import Role
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/roles")
def get_roles():
    """Retrieve all role and paginate."""
    return get_all(Role)


@app_views.route("/roles/<role_id>")
def get_role(role_id):
    """Retrieve role with role's id from model table."""
    return get_one(Role, role_id)


@app_views.route("/roles", methods=["POST"])
def create_role():
    """Create role record in model table."""
    return create_entry(Role)

@app_views.route("/roles/<role_id>", methods=["PUT"])
def update_role(role_id):
    """Update role record in model table."""
    return update_entry(Role, role_id)

@app_views.route("/roles/<role_id>", methods=["DELETE"])
def delete_role(role_id):
    """Delete role record in model table."""
    return delete_entry(Role, role_id)
