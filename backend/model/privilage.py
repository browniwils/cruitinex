#!/bin/usr/python3
"""Privilage module for crutinex application."""
from model import Base
from model.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Privilage(BaseModel, Base):
    """User type model object."""
    __tablename__ = "privilages"
    name = Column("name", String(128), nullable=False)
    roles = relationship("Role", backref="privilages")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Role(BaseModel, Base):
    """Roles table for privilage."""
    __tablename__ = "roles"
    role_type = Column("role_type", String(10), nullable=False)
    privilage_id = Column("privilage_id",
                          ForeignKey("privilages.id"), nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
