#!/bin/usr/python3
"""Module for handling employees API endpoints."""
from api.v1 import app_views
from flask import abort
from flask import jsonify
from model.user import User



@app_views.route("/employees")
def get_employees():
    """Retrieve all employees."""

    return jsonify(), 200


@app_views.route("/employees/<employee_id>")
def get_employee(employee_id):
    """Retrieve employee with employee id."""

    abort(404)

