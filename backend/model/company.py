#!/bin/usr/python3
"""Copmany module for crutinex application."""
from model import Base
from model.base_model import BaseModel
from model.address import Address
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Company(BaseModel, Base):
    """Copmany object model."""
    __tablename__ = "companies"
    name = Column("name", String(128), nullable=False)
    address = Column("address", ForeignKey("addresses.id"), nullable=False)
    website = Column("website", String(128), nullable=False)

    employees = relationship("User", backref="companies")
    departments = relationship("Department", backref="companies")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Department(BaseModel, Base):
    """Department object model."""
    __tablename__ = "departments"
    name = Column("name", String(128), nullable=False)
    company_id = Column("company_id",
                        ForeignKey("companies.id"), nullable=False)

    employees = relationship("User", backref="departments")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
