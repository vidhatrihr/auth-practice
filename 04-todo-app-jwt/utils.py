import string
import secrets
from flask import request
from models import Session
from jwt import jwt_decode


def generate_token(length=10):
  chars = string.ascii_letters + string.digits
  return ''.join(secrets.choice(chars) for _ in range(length))


def validate_session():
  jwt_token = request.cookies.get('jwt_token')  # jwt token
  if jwt_token:
    try:
      payload = jwt_decode(jwt_token)
    except:
      return None

    session = Session.query.filter_by(id=payload['session_id']).first()
    if session and session.token == payload['token']:
      return session
  return None  # Unauthorized
