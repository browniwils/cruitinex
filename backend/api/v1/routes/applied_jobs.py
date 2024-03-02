#!/bin/usr/python3
"""Module for handling applied_jobs API endpoints."""
from api.v1 import app_views
from model.job import AppliedJob
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/applied-jobs")
def get_applied_jobs():
    """Retrieve all job and paginate."""
    return get_all(AppliedJob)


@app_views.route("/applied-jobs/<applied_jobs>")
def get_applied_job(applied_jobs):
    """Retrieve job with job's id from model table."""
    return get_one(AppliedJob, applied_jobs)


@app_views.route("/applied-jobs", methods=["POST"])
@authentication_required
@authorization_required(AUTH.CREATE)
def create_applied_jobs():
    """Create job record in model table."""
    return create_entry(AppliedJob)

@app_views.route("/applied-jobs/<applied_jobs>", methods=["PUT"])
@authentication_required
@authorization_required(AUTH.UPDATE)
def update_applied_jobs(applied_jobs):
    """Update job record in model table."""
    return update_entry(AppliedJob, applied_jobs)

@app_views.route("/applied-jobs/<applied_jobs>", methods=["DELETE"])
@authentication_required
@authorization_required(AUTH.DELETE)
def delete_applied_jobs(applied_jobs):
    """Delete job record in model table."""
    return delete_entry(AppliedJob, applied_jobs)
