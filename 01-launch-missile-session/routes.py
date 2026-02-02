from flask import Blueprint, render_template, request, jsonify
from werkzeug.security import check_password_hash
from utils import generate_token
from models import db, User, Session

routes = Blueprint("routes", __name__)


@routes.route('/')
def index():
  return render_template('index.html')


@routes.route('/auth/login', methods=['POST'])
def login():
  email = request.json.get('email')
  password = request.json.get('password')

  user = User.query.filter_by(email=email).first()

  if user and check_password_hash(user.password, password):
    session = Session(
        token=generate_token(),
        user_id=user.id
    )
    db.session.add(session)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': f'Logged in as {user.name}',
        'payload': {
            'sessionId': session.id,
            'token': session.token
        }
    })
  else:
    return jsonify({
        'success': False,
        'message': 'Email or password is incorrect'
    })


@routes.route('/launch-missile')
def launch():
  session_id = request.args.get('session_id')  # args: query params
  token = request.args.get('token')

  session = Session.query.filter_by(id=session_id).first()

  if session and session.token == token:
    user = User.query.filter_by(id=session.user_id).first()
    return jsonify({
        'success': True,
        'message': f'Missile is launched 🚀 by {user.name}'
    })
  else:
    return jsonify({
        'success': False,
        'message': 'You cannot launch missile'
    }), 401
