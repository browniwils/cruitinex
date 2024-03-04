#!/bin/usr/python3
"""Module for handling jobs API endpoints."""
from api.v1 import app_views
from model.address import Address
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/addresses")
def get_jobs():
    """Retrieve all address and paginate."""
    return get_all(Address)


@app_views.route("/addresses/<address_id>")
def get_jobd(address_id):
    """Retrieve address with address's id from model table."""
    return get_one(Address, address_id)


@app_views.route("/addresses", methods=["POST"])
@authentication_required
@authorization_required(AUTH.CREATE)
def create_job():
    """Create address record in model table."""
    return create_entry(Address)

@app_views.route("/addresses/<address_id>", methods=["PUT"])
@authentication_required
@authorization_required(AUTH.UPDATE)
def update_jobd(address_id):
    """Update address record in model table."""
    return update_entry(Address, address_id)

@app_views.route("/addresses/<address_id>", methods=["DELETE"])
@authentication_required
@authorization_required(AUTH.DELETE)
def delete_jobd(address_id):
    """Delete address record in model table."""
    return delete_entry(Address, address_id)
