from flask import Blueprint
from decorators import role_required

manager_bp = Blueprint('manager', __name__, url_prefix='/manager')


# This blueprint is reserved for manager-specific routes
# that don't fit into resource-based blueprints.
