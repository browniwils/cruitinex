#!/bin/usr/python3
"""Employee module for crutinex application."""
from model import Base
from model.base_model import BaseModel


class Employee(BaseModel):
    """Employee object model."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
