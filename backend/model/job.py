#!/bin/usr/python3
"""Job module for application."""
from model import Base
from model.base_model import BaseModel


class Job(BaseModel):
    """class for Job object."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
