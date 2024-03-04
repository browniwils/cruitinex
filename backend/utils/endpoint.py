#!/bin/usr/python3
"""Helper modules for API endpoints."""
from datetime import datetime
from model.user import User
from math import ceil
from flask import abort
from flask import jsonify
from flask import request as req
from storage import db_engine


def pagination(page_start, page_size, data):
    """Handles pagination for long data."""
    total_data = len(data)
    data_start = page_start - 1
    data_end = page_size + data_start
    if total_data > page_size:
        total_page = ceil(total_data/page_size)
        current_page = data[data_start:data_end]

    if total_data <= page_size:
        total_page = 1
        current_page = data

    results = {
        "current": current_page,
        "size": len(current_page),
        "pages": total_page,
        "total": len(data)
    }
    return results

def get_all(model):
    """Get all records from model."""
    data_entries = db_engine.query(model).all()
    data = [data.view() for data in data_entries]
    paginated_data = pagination(1, 10, data)
    return jsonify(paginated_data), 200

def get_one(model, id):
    """Get one record from model."""
    data = db_engine.query(model).filter_by(id=id).first()
    if not data:
        abort(404)
    return jsonify(data.view()), 200

def create_entry(model):
    """Create new record to database."""
    body = req.get_json()
    if not body:
        abort(404)
    new_model = model(**body)
    db_engine.new(new_model).save()
    entry = db_engine.query(model).filter_by(id=new_model.id).first()
    if not entry:
        abort(400)
    return jsonify(entry.view()), 201

def update_entry(model, id):
    """Update a record in model table in db."""
    body = req.get_json()
    if not body:
        abort(400)
    entry = db_engine.query(model).filter_by(id=id).first()
    if not entry or not body.get("updated_at", None):
        abort(404)
    try:
        body.update({"updated_at": datetime.fromisoformat(
            body.get("updated_at"))})
    except ValueError:
        abort(400)
    for key, val in body.items():
        if key and key != "id":
            setattr(entry, key, val)
    db_engine.save()
    return jsonify({
        "message": "resouce updated",
        "id": entry.id
    }), 204


def delete_entry(model, id):
    """Delete a record from model table in db."""
    entry = db_engine.query(model).filter_by(id=id).first()
    if not entry:
        abort(404)
    db_engine.delete(entry).save()
    return jsonify(operation="successful",), 204


def get_workers(work_type):
    """Retrieve all works."""
    workers = db_engine.query(User).filter_by(user_type=work_type).all()
    data = [worker.view() for worker in workers]
    paginated_data = pagination(1, 10, data)
    return jsonify(paginated_data), 200
