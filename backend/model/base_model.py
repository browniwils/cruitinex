"""Base module for models."""
import json
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base user class for user models."""
    def __init__(self, *args, **kwargs) -> None:
        """Instanciate new object."""
        self.__dict__ = dict()
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.model = self.__class__.__name__

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
                self.__dict__.update({key: val})
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
                print("26", self.created_at)
                self.__dict__.update({"created_at": self.created_at})

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
                print("31",  self.updated_at)
                self.__dict__.update({"updated_at": self.updated_at})

            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
                self.__dict__.update({"id": self.id})

    def view(self):
        """Displays user data."""
        self.__dict__.update({"created_at": self.created_at.isoformat()})
        self.__dict__.update({"updated_at": self.updated_at.isoformat()})
        self.__dict__.update({"model": self.model})
        return self.__dict__
