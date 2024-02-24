#!/bin/usr/python3
"""Address module for crutinex application."""
from model import Base
from model.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Address(BaseModel, Base):
    """Addres object model."""
    __tablename__ = "addresses"
    city = Column("city", String(128), nullable=False)
    state = Column("state", String(128), nullable=False)
    zip_code = Column("zip_code", String(128), nullable=False)
    country = Column("country", String(128), nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
