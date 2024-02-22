#!/bin/usr/python3

from flask import Flask
from flask_cors import CORS
from api.v1 import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
cors = CORS(app, resources={r"/*": {"origins": ["*"]}})

app.run(debug=True)
