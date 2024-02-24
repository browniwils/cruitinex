#!/bin/usr/python3
"""User module for application."""
from model import Base
from model.base_model import BaseModel
from model.job import AppliedJob
from model.privilage import Privilage
from model.user_type import UserType
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """class for User object."""
    __tablename__ = "users"
    first_name = Column("first_name", String(128), nullable=False)
    last_name =  Column("last_name", String(128), nullable=False)
    username =  Column("username", String(128), nullable=False)
    email =  Column("email", String(128), nullable=False)
    phone =  Column("phone", String(12))
    password =  Column("password", String(128), nullable=False)
    date_of_birth = Column("date_of_birth", DateTime, nullable=False)
    address = Column("address", ForeignKey("addresses.id"))
    company_id = Column("company_id", ForeignKey("companies.id"))
    department_id = Column("department_id", ForeignKey("departments.id"))
    user_type_id = Column("user_type_id", String(36),
                          ForeignKey("user_types.id"), nullable=False)
    applied_jobs = relationship("AppliedJob", backref="users")
    privilage = Column("privilage_id",
                       ForeignKey("privilages.id"), nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
