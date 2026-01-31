from flask import Blueprint, jsonify

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/', methods=['GET'])
def index():
  return jsonify({"message": "Admin Blueprint"})
