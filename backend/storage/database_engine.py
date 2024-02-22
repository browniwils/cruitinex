#!/bin/usr/python3
"""Database module for crutinex database storing."""
from sqlalchemy import create_engine
# from model import Base


class DBStorage:
    """Database object for storing and reading data from database."""

    _db_session = ""
    _db_engine = ""

    def __init__(self, dialect: str, db_host: str, db_port: str,
                 db_user: str, db_pass: str, db_name: str) -> None:
        connect_db = f'{dialect}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        self._db_engine = create_engine(connect_db)
        self.load()

    def new(self, new_obj) -> None:
        """Stage new instance to database.
        Arg:
            new_obj: SQLAlchemy model."""

        self._db_session.add(new_obj)

    def save(self) -> None:
        """Save a staged instance to database"""
        pass

    def delete(self, obj=None) -> None:
        """Delete instance from database.
        Arg:
            new_obj: SQLAlchemy model."""

        if not obj:
            self._session.delete(obj)

    # def load(self) -> None:
    #     """Loads data from the database"""

    #     Base.metadata.create_all(self._db_engine)
    #     sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
    #     Session = scoped_session(sess_factory)
    #     self._db_session = Session
