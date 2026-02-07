from flask import Blueprint
from decorators import role_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# This blueprint is reserved for admin-specific routes
# that don't fit into resource-based blueprints.
