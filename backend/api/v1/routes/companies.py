#!/bin/usr/python3
"""Module for handling companies API endpoints."""
from api.v1 import app_views
from flask import abort
from flask import jsonify
from flask import request as req
from model.company import Company
from utils.endpoint import get_model
from storage import db_engine


@app_views.route("/companies")
def get_companies():
    """Retrieve all companies."""
    companies = get_model(Company)
    return jsonify(companies), 200


@app_views.route("/companies/<company_id>")
def get_company(company_id):
    """Retrieve company with company id."""
    company = db_engine.query(Company.__name__, id=company_id)
    if company:
        company = company(**company[0])
        return jsonify(company.view()), 200
    abort(404)


@app_views.route("/companies", methods=["POST"])
def create_company():
    """Create company resource."""
    body = req.get_json()
    if body:
        name = body.get("name", None)
        description = body.get("description", None)
        address = body.get("address", None)
        company = company(
            name=name,
            description=description,
            address=address,
        )
        company = db_engine.new(company)
        return jsonify(company), 201
    abort(404)


@app_views.route("/companies/<company_id>", methods=["PUT"])
def update_company(company_id):
    """Update company resource."""
    body = req.get_json()
    if body:
        company = db_engine.query(company.__name__, id=company_id)
        company = company[0]
        for key, val in body.items():
            if key and key != "id":
                company.update({key: val})
        results = db_engine.update(**company)
        return jsonify({
            "message": "resouce updated",
            "id": results.get("id", None)
        }), 204
    abort(404)


@app_views.route("/companies/<employe_id>", methods=["DELETE"])
def delete_company(company_id):
    """Delete company resource."""
    company = db_engine.delete(company_id)
    if company:
        return jsonify(operation="successful"), 204
    abort(404)
