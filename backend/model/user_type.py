#!/bin/usr/python3
"""User type module for crutinex application."""
from model import Base
from model.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String


class UserType(BaseModel, Base):
    """User type model object."""
    __tablename__ = "user_types"
    name = Column("name", String(128), nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
