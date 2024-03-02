"""Authentication module for protecting API endpoints."""
from flask import request as req
from flask import jsonify
from flask import abort
from functools import wraps
from model.user import User


def validate_auth(func):
    """Check for valid authentication."""
    @wraps(func)
    def decorator(*args, **kwargs):
        token = req.authorization
        if not token:
            abort(401)
        token = token.split() # split token with whitespace
        
        token = token[1] # get data in token
        decode = token # decode token with base64
        token_email = decode.get('email')
        user_roles = db_engine.query(User).filter_by(email=token_email).first().roles
        # iterate through decoded token and find user details
        # such as user id, email, username, expiration time
        # if