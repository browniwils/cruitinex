#!/bin/usr/python3
"""Module for handling employers API endpoints."""
from api.v1 import app_views
from flask import request as req
from flask import jsonify
from flask import abort
from model.employer import Employer
from utils.endpoint import get_model
from storage import db_engine


@app_views.route("/employers")
def get_employers():
    """Route for getting employers."""
    employers = get_model(Employer)
    return jsonify(employers), 200


@app_views.route("/employers/<employer_id>")
def get_employer(employer_id):
    """Retrieve an employer with id."""
    employer = db_engine.query(Employer.__name__, id=employer_id)
    if employer:
        employer = Employer(**employer[0])
        return jsonify(employer.view()), 200
    abort(404)


@app_views.route("/employers", methods=["POST"])
def create_employer():
    body = req.get_json()
    if body:
        username = body.get("username", None)
        password = body.get("password", None)
        first_name = body.get("first_name", None)
        last_name = body.get("last_name", None)
        email = body.get("email", None)
        company_id = body.get("company_id", None)
        new_employer = Employer(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_id=company_id
        )
        results = db_engine.new(new_employer)
        return jsonify(results), 201
    abort(400)

@app_views.route("/employers/<employer_id>", methods=["PUT"])
def update_employer(employer_id):
    body = req.get_json()
    if body:
        employer = db_engine.query("Employer", id=employer_id)
        employer = employer[0]
        for key, val in body.items():
            if key and key != "id":
                employer.update({key: val})
        results = db_engine.update(**employer)
        return jsonify({
            "message": "resource updated",
            "id": results.get("id", None)
        }), 204
    abort(404)

@app_views.route("/employers/<employer_id>", methods=["DELETE"])
def delete_employer(employer_id):
    employer = db_engine.delete(employer_id)
    if employer:
        return jsonify(operation="successful"), 204
    abort(404)
