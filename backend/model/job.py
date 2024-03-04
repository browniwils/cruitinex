#!/bin/usr/python3
"""Job module for application."""
from model import Base
from model.base_model import BaseModel
# from model.user import User
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String


class Job(BaseModel, Base):
    """class for Job object."""
    __tablename__ = "jobs"
    title = Column("title", String(128), nullable=False)
    description = Column("description", String(), nullable=False)
    salary = Column("salary", Integer)
    type = Column("type", Enum("on-site", "remote", "hybrid"))
    dead_line = Column("dead_line", DateTime, nullable=False)
    user_id = Column("user_id", ForeignKey("users.id"), nullable=False)
    address_id = Column("address_id", ForeignKey("addresses.id"))

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class AppliedJob(BaseModel, Base):
    """class for applied jobs."""
    __tablename__ = "applied_jobs"
    resume = Column("resume", String(), nullable=False)
    cover_letter = Column("cover_letter", String())
    job_id = Column("job_id", ForeignKey("jobs.id"), nullable=False)
    user_id = Column("user_id", ForeignKey("users.id"), nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
