#!/bin/usr/python3
"""Module for handling jobs API endpoints."""
from api.v1 import app_views
from flask import abort
from flask import jsonify
from flask import request as req
from model.job import Job
from utils.endpoint import get_model
from storage import db_engine


@app_views.route("/jobs")
def get_jobs():
    """Retrieve all jobs."""
    jobs = get_model(Job)
    return jsonify(jobs), 200


@app_views.route("/jobs/<job_id>")
def get_job(job_id):
    """Retrieve job with job id."""
    job = db_engine.query(Job.__name__, id=job_id)
    if job:
        job = job(**job[0])
        return jsonify(job.view()), 200
    abort(404)


@app_views.route("/jobs", methods=["POST"])
def create_job():
    """Create job resource."""
    body = req.get_json()
    if body:
        title = body.get("title", None)
        description = body.get("description", None)
        dead_line = body.get("dead_line", None)
        job = job(
            title=title,
            description=description,
            dead_line=dead_line,
        )
        job = db_engine.new(job)
        return jsonify(job), 201
    abort(404)


@app_views.route("/jobs/<job_id>", methods=["PUT"])
def update_job(job_id):
    """Update job resource."""
    body = req.get_json()
    if body:
        job = db_engine.query(Job.__name__, id=job_id)
        job = job[0]
        for key, val in body.items():
            if key and key != "id":
                job.update({key: val})
        results = db_engine.update(**job)
        return jsonify({
            "message": "resouce updated",
            "id": results.get("id", None)
        }), 204
    abort(404)


@app_views.route("/jobs/<employe_id>", methods=["DELETE"])
def delete_job(job_id):
    """Delete job resource."""
    job = db_engine.delete(job_id)
    if job:
        return jsonify(operation="successful"), 204
    abort(404)
