#!/bin/usr/python3
"""Helper modules for API endpoints."""
from storage import db_engine


def get_model(obj):
    """Helper for getting all model entries and its metrics."""
    if obj:
        obj_name = obj.__name__
        items = db_engine.query(obj_name)
        return {
            obj_name: items,
            "total": len(items),
            "status": "okay",
        }
