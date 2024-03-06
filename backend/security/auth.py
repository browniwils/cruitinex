"""Authentication module for protecting API endpoints."""
from api.v1.routes.index import FORBIDDEN_CODE
from api.v1.routes.index import UNAUTHORIZED_CODE
from datetime import datetime
from datetime import timedelta
from flask import abort
from flask import jsonify
from flask import request as req
from functools import wraps
from model.privilege import Privilege
from model.user import User
from storage import db_engine


TOKEN_SIZE = 2

def authentication_required(func):
    """Check for valid authentication."""
    @wraps(func)
    def decorator(*args, **kwargs):
        token = str(req.authorization)
        if not token or "bearer" not in token.lower():
            abort(FORBIDDEN_CODE)

        token = token.split()
        if len(token) != TOKEN_SIZE:
            abort(FORBIDDEN_CODE)

        session_token = token[1]
        user = db_engine.query(User).filter_by(
            session_token=session_token).first()
        if not user:
            abort(FORBIDDEN_CODE)

        now = datetime.now()
        expires_at = user.updated_at + timedelta(days=1.5)
        if now >= expires_at:
            user.session_token = None
            db_engine.save()
            return jsonify({"message": "Session Expired!"}), UNAUTHORIZED_CODE
        return func(*args, **kwargs)
    return decorator

def authorization_required(auth):
    """Check for valid authorizations."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            session_token = req.cookies.get("session_id")
            if not session_token:
                abort(UNAUTHORIZED_CODE)

            user = db_engine.query(User).filter_by(
                session_token=session_token).first()
            if not user:
                abort(UNAUTHORIZED_CODE)

            if user.session_token == "NULL":
                abort(UNAUTHORIZED_CODE)

            if user.session_token != session_token:
                abort(UNAUTHORIZED_CODE)

            user_auths = db_engine.query(Privilege).filter_by(
                id=user.privilage_id).first().roles
            if not user_auths:
                abort(UNAUTHORIZED_CODE)
            auths = [role.name for role in user_auths]
            if auth not in auths:
                abort(UNAUTHORIZED_CODE)
            return func(*args, **kwargs)
        return wrapper
    return decorator


class AUTH:
    READ = "read"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"

