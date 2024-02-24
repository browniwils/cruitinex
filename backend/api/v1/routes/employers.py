#!/bin/usr/python3
"""Module for handling employers API endpoints."""
from api.v1 import app_views
from flask import jsonify
from flask import abort
from model.user import User


@app_views.route("/employers")
def get_employers():
    """Route for getting employers."""

    return jsonify(), 200


@app_views.route("/employers/<employer_id>")
def get_employer(employer_id):
    """Retrieve an employer with id."""

    abort(404)

