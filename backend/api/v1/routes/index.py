#!/bin/usr/python3

from api.v1 import app_views
from flask import jsonify


@app_views.route("/")
def status():
    """Route handling the status of ApI."""
    return jsonify({"status": "okay"}), 200


@app_views.errorhandler(404)
def resouce_not_found(error):
    """Handle not found resources."""
    return jsonify({"message": "resource not found."})


@app_views.errorhandler(400)
def field_error(error):
    """Resource creation error."""
    jsonify(
        {"message": "missing information in request."
         }), 400