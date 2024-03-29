#!/bin/usr/python3
"""Module for handling jobs API endpoints."""
from api.v1 import app_views
from model.job import Job
from security.auth import AUTH
from security.auth import authentication_required
from security.auth import authorization_required
from utils.endpoint import create_entry
from utils.endpoint import delete_entry
from utils.endpoint import get_all
from utils.endpoint import get_one
from utils.endpoint import update_entry


@app_views.route("/jobs")
def get_jobs():
    """Retrieve all job and paginate."""
    return get_all(Job)


@app_views.route("/jobs/<job_id>")
def get_job(job_id):
    """Retrieve job with job's id from model table."""
    return get_one(Job, job_id)


@app_views.route("/jobs", methods=["POST"])
@authentication_required
@authorization_required(AUTH.CREATE)
def create_job():
    """Create job record in model table."""
    return create_entry(Job)

@app_views.route("/jobs/<job_id>", methods=["PUT"])
@authentication_required
@authorization_required(AUTH.UPDATE)
def update_job(job_id):
    """Update job record in model table."""
    return update_entry(Job, job_id)

@app_views.route("/jobs/<job_id>", methods=["DELETE"])
@authentication_required
@authorization_required(AUTH.DELETE)
def delete_job(job_id):
    """Delete job record in model table."""
    return delete_entry(Job, job_id)
