#!/bin/usr/python3
"""Module for handling companies API endpoints."""
from api.v1 import app_views
from model.company import Company
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/companies")
@authentication_required
@authorization_required(AUTH.READ)
def get_companies():
    """Retrieve all companies and paginate."""
    return get_all(Company)


@app_views.route("/companies/<company_id>")
@authentication_required
@authorization_required(AUTH.READ)
def get_company(company_id):
    """Retrieve company with company id from db."""
    return get_one(Company, company_id)


@app_views.route("/companies", methods=["POST"])
@authentication_required
@authorization_required(AUTH.CREATE)
def create_company():
    """Create company record in model table."""
    return create_entry(Company)


@app_views.route("/companies/<company_id>", methods=["PUT"])
@authentication_required
@authorization_required(AUTH.UPDATE)
def update_company(company_id):
    """Update company record in model table."""
    return update_entry(Company, company_id)


@app_views.route("/companies/<company_id>", methods=["DELETE"])
@authentication_required
@authorization_required(AUTH.DELETE)
def delete_company(company_id):
    """Delete company record in model table."""
    return delete_entry(Company, company_id)
