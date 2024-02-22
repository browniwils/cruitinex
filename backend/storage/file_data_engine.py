#!/bin/usr/python3
"""File storage module for crutinex data storing."""
import json


class FileStorage:
    """File database object for storing and reading data from database."""
    __file_db_name = 'database.json'
    __data = []

    def __init__(self):
        """Instanciate file database object."""
        self.load()

    def new(self, new_obj):
        """Create new object for storing."""
        if new_obj.id:
            obj_data = new_obj.view()
            self.__data.append(obj_data)
            self.save()
            return obj_data

    def save(self) -> None:
        """Save a object data to file storage."""
        with open(self.__file_db_name, "w") as file:
            file.write(json.dumps(self.__data))
        self.load()

    def update(self, **kwargs):
        """Update object in storage."""
        for idx, data in enumerate(self.__data):
            if kwargs.get("id", None) == data.get("id"):
                for key, val in kwargs.items():
                    self.__data[idx].update({key: val})
                self.save()
                return self.__data[idx]

    def delete(self, id=None) -> None:
        """Delete object from file data storage."""
        if id:
            for idx, data in enumerate(self.__data):
                if data.get("id", None) == id:
                    del self.__data[idx]
                    self.save()
                    return True
                return False

    def load(self) -> None:
        """Loads data from the file data storage."""
        try:
            with open(self.__file_db_name, "r") as file:
                self.__data = json.load(file)
        except FileNotFoundError:
            with open(self.__file_db_name, "w") as file:
                file.write(json.dumps([]))
        except json.JSONDecodeError:
            return

    def query(self, *model_args, **kwargs):
        """Retrieve model objects from storage."""
        if not model_args:
            return self.__data
        data = []
        for entry in self.__data:
            if entry.get("model", None) in model_args:
                if kwargs:
                    for key, val in kwargs.items():
                        if val in str(data):
                            continue
                        if entry.get(key, None) == val:
                            data.append(entry)
                if not kwargs:
                    data.append(entry)
        return data