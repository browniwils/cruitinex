"""Base module for models."""
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String


class BaseModel:
    """Base user class for user models."""
    id = Column("id", String(36), primary_key=True)
    created_at = Column("created_at", DateTime, default=datetime.utcnow())
    updated_at = Column("updated_at", DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs) -> None:
        """Instanciate new object."""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.fromisoformat(
                    kwargs.get("created_at"))

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.fromisoformat(
                    kwargs.get("updated_at"))

            if kwargs.get("id", None) is None:
                self.id = str(uuid4())

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def view(self):
        """Displays user data."""
        view_properties = self.__dict__.copy()
        if "_sa_instance_state" in view_properties.keys():
            del view_properties["_sa_instance_state"]
        if "__password" in view_properties.keys():
            del view_properties["__password"]
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                view_properties.update({key: value.isoformat()})

        return view_properties
