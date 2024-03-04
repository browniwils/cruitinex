#!/bin/usr/python3
"""Privilage module for crutinex application."""
from model import Base
from model.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship


class Privilege(BaseModel, Base):
    """User type model object."""
    __tablename__ = "privileges"
    name = Column("name", String(128), nullable=False)

    roles = relationship("Role", secondary="privilege_role")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Role(BaseModel, Base):
    """Roles table for privilege."""
    __tablename__ = "roles"
    name = Column("role", String(10), nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


privilege_role = Table('privilege_role', Base.metadata,
    Column('privilege_id', Integer, ForeignKey('privileges.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)