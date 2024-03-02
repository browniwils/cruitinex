#!/bin/usr/python3
"""Module for handling departments API endpoints."""
from api.v1 import app_views
from model.company import Department
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/departments")
@authentication_required
@authorization_required(AUTH.READ)
def get_departments():
    """Retrieve all departments and paginate."""
    return get_all(Department)


@app_views.route("/departments/<department_id>")
@authentication_required
@authorization_required(AUTH.READ)
def get_department(department_id):
    """Retrieve departments with departments id from db."""
    return get_one(Department, department_id)


@app_views.route("/departments", methods=["POST"])
@authentication_required
@authorization_required(AUTH.CREATE)
def create_department():
    """Create departments record in model table."""
    return create_entry(Department)


@app_views.route("/departments/<department_id>", methods=["PUT"])
@authentication_required
@authorization_required(AUTH.UPDATE)
def update_department(department_id):
    """Update departments record in model table."""
    return update_entry(Department, department_id)


@app_views.route("/departments/<department_id>", methods=["DELETE"])
@authentication_required
@authorization_required(AUTH.DELETE)
def delete_department(department_id):
    """Delete departments record in model table."""
    return delete_entry(Department, department_id)
