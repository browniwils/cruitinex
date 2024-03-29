#!/bin/usr/python3
"""Application server."""
from flask import Flask
from flask_cors import CORS
from api.v1 import app_views
from utils.script import add_admin_user


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


if __name__ == "__main__":
    add_admin_user()
    app.run(debug=True)
