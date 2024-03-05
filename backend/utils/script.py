#!/bin/usr/python3
"""Module for basic operation for system initiation and testing."""
from model.user import User
from model.user_type import UserType
from model.privilege import Privilege
from model.privilege import Role
from storage import db_engine


def add_admin_user():
    """Checks and add superuser aka admin if doesn't exist."""
    add_uesr_types(["Employer", "Employee", "Admin"])
    admin = db_engine.query(User).filter_by(username="admin").first()
    if admin:
        return
    admin = User(
        first_name="Admin",
        last_name="",
        password="admin123",
        email="admin@cruitinex.local",
        username="admin",
        gender="M"
    )
    roles = ["read", "create", "update", "delete"]
    roles = add_roles(roles)
    privilege = Privilege(name="admin", roles=roles)
    db_engine.new(privilege).save()
    admin.privilage_id = privilege.id
    user_type = db_engine.query(UserType).filter_by(name="Admin").first()
    admin.user_type_id = user_type.id
    db_engine.new(admin).save()

def add_roles(roles):
    """Checks and add roles if aren't present."""
    all_roles = db_engine.query(Role).all()
    roles_names = [r.name for r in all_roles]
    for role in roles:
        if role in roles_names:
            continue
        new_role = Role(name=role)
        db_engine.new(new_role).save()
        all_roles.append(new_role)
    return all_roles

def add_uesr_types(_types):
    """Checks and add user types if doesn't exist."""
    user_types = db_engine.query(UserType).all()
    types = [ut.name for ut in user_types]
    for _type in _types:
        if _type in types:
            continue
        new_type = UserType(name=_type)
        db_engine.new(new_type).save()
        user_types.append(new_type)
