from functools import wraps
from flask import jsonify, request
from jwt import jwt_decode


def login_required(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    jwt = request.cookies.get('jwt')
    if jwt:
      try:
        payload = jwt_decode(jwt)
        return fn(payload['user_id'], *args, **kwargs)
      except Exception as e:
        print(e)
    return jsonify({'success': False, 'message': 'Unauthorized'}), 401

  return wrapper
