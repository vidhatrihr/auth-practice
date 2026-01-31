from flask import Blueprint, jsonify

manager_bp = Blueprint('manager', __name__, url_prefix='/manager')


@manager_bp.route('/', methods=['GET'])
def index():
  return jsonify({"message": "Manager Blueprint"})
