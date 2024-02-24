#!/bin/usr/python3
"""Module for handling privileges API endpoints."""
from api.v1 import app_views
from model.privilage import Privilage
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/privileges")
def get_privileges():
    """Retrieve all privilege and paginate."""
    return get_all(Privilage)


@app_views.route("/privileges/<privilege_id>")
def get_privilege(privilege_id):
    """Retrieve privilege with privilege's id from model table."""
    return get_one(Privilage, privilege_id)


@app_views.route("/privileges", methods=["POST"])
def create_privilege():
    """Create privilege record in model table."""
    return create_entry(Privilage)

@app_views.route("/privileges/<privilege_id>", methods=["PUT"])
def update_privilege(privilege_id):
    """Update privilege record in model table."""
    return update_entry(Privilage, privilege_id)

@app_views.route("/privileges/<privilege_id>", methods=["DELETE"])
def delete_privilege(privilege_id):
    """Delete privilege record in model table."""
    return delete_entry(Privilage, privilege_id)
