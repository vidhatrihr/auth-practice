from flask import Blueprint, jsonify, request
from models import db, Supplier
from decorators import role_required

suppliers_bp = Blueprint('suppliers', __name__, url_prefix='/suppliers')


@suppliers_bp.route('', methods=['GET'])
@role_required(['admin', 'manager'])
def list_suppliers(payload):
  suppliers = Supplier.query.all()

  return jsonify({
      'success': True,
      'message': 'All suppliers fetched',
      'payload': {
          'suppliers': [
              {'id': s.id, 'name': s.name}
              for s in suppliers
          ]
      }
  })


@suppliers_bp.route('', methods=['POST'])
@role_required('admin')
def create_supplier(payload):
  name = request.json.get('name')

  supplier = Supplier(name=name)
  db.session.add(supplier)
  db.session.commit()

  return jsonify({
      'success': True,
      'message': 'Supplier created',
      'payload': {'supplierId': supplier.id}
  })


@suppliers_bp.route('/<int:supplier_id>', methods=['DELETE'])
@role_required('admin')
def delete_supplier(payload, supplier_id):
  supplier = Supplier.query.filter_by(id=supplier_id).first()

  if not supplier:
    return jsonify({'success': False, 'message': 'Supplier not found'}), 404

  # Check if supplier has orders
  if supplier.orders:
    return jsonify({'success': False, 'message': 'Cannot delete supplier with existing orders'}), 400

  db.session.delete(supplier)
  db.session.commit()

  return jsonify({'success': True, 'message': 'Supplier deleted'})
