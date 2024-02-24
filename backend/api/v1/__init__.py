#!/bin/usr/python3
"""API blueprint module."""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.routes.applied_jobs import *
from api.v1.routes.companies import *
from api.v1.routes.departments import *
from api.v1.routes.employees import *
from api.v1.routes.employers import *
from api.v1.routes.index import *
from api.v1.routes.jobs import *
from api.v1.routes.privileges import *
from api.v1.routes.roles import *
from api.v1.routes.users import *
