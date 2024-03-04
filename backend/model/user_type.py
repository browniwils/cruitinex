#!/bin/usr/python3
"""User type module for crutinex application."""
from model import Base
from model.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy.orm import relationship


class UserType(BaseModel, Base):
    """User type model object."""
    __tablename__ = "user_types"
    name = Column("name", Enum("Employer", "Employee", "Admin"),
                  nullable=False)

    users = relationship("User", backref="user_types")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
