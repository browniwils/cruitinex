#!/bin/usr/python3
"""Module for handling employers API endpoints."""
from api.v1 import app_views
from model.user import User
from utils.endpoint import create_entry


@app_views.route("/employers", methods=["POST"])
def create_employers():
    """Create user record in model table."""
    return create_entry(User)
