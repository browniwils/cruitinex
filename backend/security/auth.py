"""Authentication module for protecting API endpoints."""
import json
from api.v1.routes.index import FORBIDDEN_CODE
from api.v1.routes.index import UNAUTHORIZED_CODE
from base64 import b64decode
from datetime import datetime
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

        request_token = token[1]
        decode_request_session = b64decode(request_token.encode()).decode()
        decode_request_session = json.loads(decode_request_session)

        user_email = decode_request_session.get("email")
        if not user_email:
            abort(FORBIDDEN_CODE)

        request_session_token = decode_request_session.get("session_token")
        if not request_session_token:
            abort(FORBIDDEN_CODE)

        user = db_engine.query(User).filter_by(email=user_email).first()
        if not user:
            abort(FORBIDDEN_CODE)

        if not user.session_token:
            abort(FORBIDDEN_CODE)

        user_session = user.session_token
        decode_user_session = b64decode(user_session.encode())
        decode_user_session = json.loads(decode_user_session.decode())
        user_session_token = decode_user_session.get("session_token")
        if not user_session_token:
            abort(FORBIDDEN_CODE)
    
        if user_session_token != request_session_token:
            abort(FORBIDDEN_CODE)

        session_expires_at = decode_user_session.get("session_expires_at")
        if not session_expires_at:
            abort(FORBIDDEN_CODE)

        now = datetime.now()
        expires_at = datetime.fromisoformat(session_expires_at)
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

            decoded_token = b64decode(session_token.encode())
            decoded_token = json.loads(decoded_token.decode())
            session_token_id = decoded_token.get("session_token")
            if not session_token_id:
                abort(UNAUTHORIZED_CODE)

            user_session_token = b64decode(user.session_token.encode())
            user_session_token = json.loads(user_session_token.decode())
            user_session_token_id = decoded_token.get("session_token")
            if not user_session_token_id:
                abort(UNAUTHORIZED_CODE)

            if user_session_token_id != session_token_id:
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

