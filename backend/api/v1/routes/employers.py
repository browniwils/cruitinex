#!/bin/usr/python3
"""Module for handling employers API endpoints."""
from api.v1 import app_views
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import get_workers


@app_views.route("/employers")
@authentication_required
@authorization_required(AUTH.READ)
def get_employers():
    """Retrieve all employers."""
    return get_workers("Employer")

