#!/bin/usr/python3
"""Database module for crutinex database storing."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from model import Base


class DBStorage:
    """Database object for storing and reading data from database."""

    _db_session = ""
    _db_engine = ""

    def __init__(self, *args, **kwargs):
        # connect_db = "{}+{}://{}:{}@{}:{}/{}".format(
        #     driver, dialect, db_user, db_pass,
        #     db_host, db_port, db_name
        # )
        connect_db = "sqlite:///sample.db"
        self._db_engine = create_engine(connect_db, pool_size=2000)
        self.load()

    def new(self, new_obj):
        """Stage new instance to database.
        Arg:
            new_obj: SQLAlchemy model object."""
        self._db_session.add(new_obj)
        return self

    def save(self) -> None:
        """Save a staged instance to database"""
        self._db_session.commit()

    def delete(self, obj=None):
        """Delete instance from database.
        Arg:
            new_obj: SQLAlchemy model object."""
        if obj:
            self._db_session.delete(obj)
        return self

    # def update(self, **kwargs):
    #     """Update instance."""
    #     self.query()

    def rollback(self):
        """Rolls back current transaction."""
        self._db_session.rollback()

    def close(self):
        """Removes method on the private session attribute"""
        self._db_session.remove()

    def load(self):
        """Loads data from the database"""
        Base.metadata.create_all(self._db_engine)
        sess_factory = sessionmaker(bind=self._db_engine,
                                    expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self._db_session = Session

    def query(self, query):
        """Query database."""
        return self._db_session.query(query)
