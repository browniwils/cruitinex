"""Authentication module for protecting API endpoints."""
from base64 import b64decode
from flask import abort
from flask import request as req
from functools import wraps
from model.privilege import Privilege
from model.user import User
from storage import db_engine


def authentication_required(func):
    """Check for valid authentication."""
    @wraps(func)
    def decorator(*args, **kwargs):
        token = req.authorization
        if not token or "bearer" not in token.lower():
            abort(401)

        token = token.split() # split token with whitespace

        token = token[1] # get data in token
        decode = b64decode(token.encode()).decode() # decode token with base64
        # iterate through decoded token and find user details
        # such as user id, email, username, expiration time
        # token_email = decode.get('email')
        user = db_engine.query(User)
        user = user.filter_by(email=decode).first()
        if not user:
            abort(401)
        return func
    return decorator

def authorization_required(auth):
    """Check for valid authorizations."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            session_token = req.cookies.get("session_id")
            if not session_token:
                abort(401)
            decoded_token = b64decode(session_token.encode()).decode()
            user = db_engine.query(User).filter_by(
                session_token=decoded_token).first()
            if not user:
                abort(401)
            user_auths = db_engine.query(Privilege).filter_by(
                id=user.id).first().roles
            auths = [role.name for role in user_auths]
            if auth not in auths:
                abort(401)
            return func
        return wrapper
    return decorator


class AUTH:
    READ = "read"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"

