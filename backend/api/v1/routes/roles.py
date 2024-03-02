#!/bin/usr/python3
"""Module for handling roles API endpoints."""
from api.v1 import app_views
from model.privilege import Role
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/roles")
@authentication_required
@authorization_required(AUTH.READ)
def get_roles():
    """Retrieve all role and paginate."""
    return get_all(Role)


@app_views.route("/roles/<role_id>")
@authentication_required
@authorization_required(AUTH.READ)
def get_role(role_id):
    """Retrieve role with role's id from model table."""
    return get_one(Role, role_id)


@app_views.route("/roles", methods=["POST"])
@authentication_required
@authorization_required(AUTH.CREATE)
def create_role():
    """Create role record in model table."""
    return create_entry(Role)

@app_views.route("/roles/<role_id>", methods=["PUT"])
@authentication_required
@authorization_required(AUTH.UPDATE)
def update_role(role_id):
    """Update role record in model table."""
    return update_entry(Role, role_id)

@app_views.route("/roles/<role_id>", methods=["DELETE"])
@authentication_required
@authorization_required(AUTH.DELETE)
def delete_role(role_id):
    """Delete role record in model table."""
    return delete_entry(Role, role_id)
