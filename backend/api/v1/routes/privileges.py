#!/bin/usr/python3
"""Module for handling privileges API endpoints."""
from api.v1 import app_views
from model.privilege import Privilege
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/privileges")
@authentication_required
@authorization_required(AUTH.READ)
def get_privileges():
    """Retrieve all privilege and paginate."""
    return get_all(Privilege)


@app_views.route("/privileges/<privilege_id>")
@authentication_required
@authorization_required(AUTH.READ)
def get_privilege(privilege_id):
    """Retrieve privilege with privilege's id from model table."""
    return get_one(Privilege, privilege_id)


@app_views.route("/privileges", methods=["POST"])
@authentication_required
@authorization_required(AUTH.CREATE)
def create_privilege():
    """Create privilege record in model table."""
    return create_entry(Privilege)

@app_views.route("/privileges/<privilege_id>", methods=["PUT"])
@authentication_required
@authorization_required(AUTH.UPDATE)
def update_privilege(privilege_id):
    """Update privilege record in model table."""
    return update_entry(Privilege, privilege_id)

@app_views.route("/privileges/<privilege_id>", methods=["DELETE"])
@authentication_required
@authorization_required(AUTH.DELETE)
def delete_privilege(privilege_id):
    """Delete privilege record in model table."""
    return delete_entry(Privilege, privilege_id)
