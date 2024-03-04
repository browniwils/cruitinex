#!/bin/usr/python3
"""Address module for crutinex application."""
from model import Base
from model.base_model import BaseModel
from model.job import Job
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

    companies = relationship("Company", backref="addresses")
    users = relationship("User", backref="addresses")
    jobs = relationship("Job", backref="addresses")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
