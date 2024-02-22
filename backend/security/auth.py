"""Authentication module for protecting API endpoints."""
from flask import request as req
from flask import jsonify
from functools import wraps


def validate_auth(func):
    """Check for valid authentication."""
    @wraps(func)
    def decorator(*args, **kwargs):
        ...