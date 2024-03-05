#!/bin/usr/python3
"""Module for handling general API endpoints."""
from api.v1 import app_views
from flask import jsonify

BAD_REQUEST_CODE = 400
FORBIDDEN_CODE = 403
NOT_FOUND_CODE = 404
UNAUTHORIZED_CODE = 401

@app_views.route("/app-status")
def status():
    """Route handling the status of ApI."""
    return jsonify({"status": "okay",
                    "message": "api is working fine"}), 200


@app_views.errorhandler(BAD_REQUEST_CODE)
def bad_request(error):
    """Handles bad request error."""
    return jsonify({"message": "Bad Request."}), BAD_REQUEST_CODE


@app_views.errorhandler(UNAUTHORIZED_CODE)
def unauthorized(error):
    """Handles unauthorized request error."""
    return jsonify({"message": "Unauthorized."}), UNAUTHORIZED_CODE


@app_views.errorhandler(FORBIDDEN_CODE)
def forbidden(error):
    """Handles forbidden request error."""
    return jsonify({"message": "Forbidden."}), FORBIDDEN_CODE


@app_views.errorhandler(NOT_FOUND_CODE)
def not_found(error):
    """Handle not found error."""
    return jsonify({"message": "Not Found."}), NOT_FOUND_CODE

