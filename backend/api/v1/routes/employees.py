#!/bin/usr/python3
"""Module for handling employees API endpoints."""
from api.v1 import app_views
from flask import abort
from flask import jsonify
from flask import request as req
from model.employee import Employee
from utils.endpoint import get_model
from storage import db_engine


@app_views.route("/employees")
def get_employees():
    """Retrieve all employees."""
    employees = get_model(Employee)
    return jsonify(employees), 200


@app_views.route("/employees/<employee_id>")
def get_employee(employee_id):
    """Retrieve employee with employee id."""
    employee = db_engine.query(Employee.__name__, id=employee_id)
    if employee:
        employee = Employee(**employee[0])
        return jsonify(employee.view()), 200
    abort(404)


@app_views.route("/employees", methods=["POST"])
def create_employee():
    """Create employee resource."""
    body = req.get_json()
    if body:
        username = body.get("username", None)
        password = body.get("password", None)
        first_name = body.get("first_name", None)
        last_name = body.get("last_name", None)
        email = body.get("email", None)
        company_id = body.get("company_id", None)
        employee = Employee(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_id=company_id
        )
        employee = db_engine.new(employee)
        return jsonify(employee), 201
    abort(404)


@app_views.route("/employees/<employee_id>", methods=["PUT"])
def update_employee(employee_id):
    """Update employee resource."""
    body = req.get_json()
    if body:
        employee = db_engine.query(Employee.__name__, id=employee_id)
        employee = employee[0]
        for key, val in body.items():
            if key and key != "id":
                employee.update({key: val})
        results = db_engine.update(**employee)
        return jsonify({
            "message": "resouce updated",
            "id": results.get("id", None)
        }), 204
    abort(404)


@app_views.route("/employees/<employe_id>", methods=["DELETE"])
def delete_employee(employee_id):
    """Delete employee resource."""
    employee = db_engine.delete(employee_id)
    if employee:
        return jsonify(operation="successful"), 204
    abort(404)
