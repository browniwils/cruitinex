#!/bin/usr/python3
"""Employer module for crutinex application."""
from model import Base
from model.base_model import BaseModel


class Employer(BaseModel):
    """Employer model object."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
