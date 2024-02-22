#!/bin/usr/python3
"""User module for application."""
from model import Base
from model.base_model import BaseModel


class User(BaseModel):
    """class for User object."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
