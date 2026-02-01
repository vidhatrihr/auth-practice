import time
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from models import db, User, Session
from jwt import jwt_encode
from decorators import login_required

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/whoami')
@login_required()
def whoami(payload):
  user = User.query.filter_by(id=payload['user_id']).first()
  return jsonify({
      'success': True,
      'message': f'Logged in as {user.name}',
      'data': {
          'name': user.name,
          'role': user.role
      },
      'sessions': [{
          'session_id': s.id,
          'date_created': s.date_created
      } for s in user.sessions]
  })


@auth_bp.route('/login', methods=['POST'])
def login():
  email = request.json.get('email')
  password = request.json.get('password')

  user = User.query.filter_by(email=email).first()

  if user and check_password_hash(user.password, password):
    session = Session(user_id=user.id)
    db.session.add(session)
    db.session.commit()

    payload = {
        'user_id': user.id,
        'role': user.role,
        'iat': int(time.time()),
        "session_id": session.id,
    }
    jwt = jwt_encode(payload)

    return jsonify({
        'success': True,
        'message': f'Logged in as {user.name}',
        'data': {
            'token': jwt,
            'name': user.name,
            'role': user.role
        }
    })
  else:
    return jsonify({
        'success': False,
        'message': 'Email or password incorrect'
    }), 401


@auth_bp.route('/logout')
@login_required()
def logout(payload):
  # Delete current session
  session = Session.query.filter_by(id=payload['session_id']).first()
  if session:
    db.session.delete(session)
    db.session.commit()

  response = jsonify({'success': True, 'message': 'Logged out'})
  return response


@auth_bp.route('/logout-everywhere')
@login_required()
def logout_everywhere(payload):
  # Delete all sessions for the given user
  Session.query.filter_by(user_id=payload['user_id']).delete()
  db.session.commit()

  response = jsonify({'success': True, 'message': 'Logged out from everywhere'})
  return response
