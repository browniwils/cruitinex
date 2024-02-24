#!/bin/usr/python3
"""Module for handling general API endpoints."""
from api.v1 import app_views
from flask import jsonify


@app_views.route("/app-status")
def status():
    """Route handling the status of ApI."""
    return jsonify({"status": "okay",
                    "message": "api is working fine"}), 200


@app_views.errorhandler(400)
def field_error(error):
    """Handles bad request error."""
    return jsonify( {"message": "Bad request."}), 400


@app_views.errorhandler(401)
def field_error(error):
    """Handles unauthorized request error."""
    return jsonify( {"message": "Unauthorized."}), 401


@app_views.errorhandler(403)
def field_error(error):
    """Handles forbidden request error."""
    return jsonify( {"message": "Forbidden."}), 403


@app_views.errorhandler(404)
def resouce_not_found(error):
    """Handle not found error."""
    return jsonify({"message": "Not Found."}), 404

