from flask import Blueprint, jsonify, request
from models import db, Customer
from decorators import role_required

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')


@customers_bp.route('', methods=['GET'])
@role_required(['admin', 'manager'])
def list_customers(payload):
  customers = Customer.query.all()

  return jsonify({
      'success': True,
      'message': 'All customers fetched',
      'payload': {
          'customers': [
              {'id': c.id, 'name': c.name}
              for c in customers
          ]
      }
  })


@customers_bp.route('', methods=['POST'])
@role_required('admin')
def create_customer(payload):
  name = request.json.get('name')

  customer = Customer(name=name)
  db.session.add(customer)
  db.session.commit()

  return jsonify({
      'success': True,
      'message': 'Customer created',
      'payload': {'customerId': customer.id}
  })


@customers_bp.route('/<int:customer_id>', methods=['DELETE'])
@role_required('admin')
def delete_customer(payload, customer_id):
  customer = Customer.query.filter_by(id=customer_id).first()

  if not customer:
    return jsonify({'success': False, 'message': 'Customer not found'}), 404

  # Check if customer has orders
  if customer.orders:
    return jsonify({'success': False, 'message': 'Cannot delete customer with existing orders'}), 400

  db.session.delete(customer)
  db.session.commit()

  return jsonify({'success': True, 'message': 'Customer deleted'})
