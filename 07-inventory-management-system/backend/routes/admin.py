from flask import Blueprint, jsonify, request
from models import db, Product, Customer, Supplier, OrderItem
from decorators import login_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# ========== PRODUCTS ==========

@admin_bp.route('/products', methods=['GET'])
@login_required('admin')
def list_products(payload):
  products = Product.query.all()

  return jsonify({
      'success': True,
      'message': 'All products fetched',
      'payload': {
          'products': [
              {
                  'id': product.id,
                  'name': product.name,
                  'costPrice': product.cost_price,
                  'sellingPrice': product.selling_price,
                  'qtyAvailable': product.qty_available,
              }
              for product in products
          ]
      }
  })


@admin_bp.route('/products', methods=['POST'])
@login_required('admin')
def create_product(payload):
  name = request.json.get('name')
  cost_price = request.json.get('costPrice')
  selling_price = request.json.get('sellingPrice')
  qty_available = request.json.get('qtyAvailable', 0)

  product = Product(
      name=name,
      cost_price=cost_price,
      selling_price=selling_price,
      qty_available=qty_available,
  )
  db.session.add(product)
  db.session.commit()

  return jsonify({
      'success': True,
      'message': 'Product created',
      'payload': {'productId': product.id}
  })


@admin_bp.route('/products/<int:product_id>', methods=['PATCH'])
@login_required('admin')
def update_product(payload, product_id):
  product = Product.query.filter_by(id=product_id).first()

  if not product:
    return jsonify({'success': False, 'message': 'Product not found'}), 404

  if 'name' in request.json:
    product.name = request.json.get('name')
  if 'costPrice' in request.json:
    product.cost_price = request.json.get('costPrice')
  if 'sellingPrice' in request.json:
    product.selling_price = request.json.get('sellingPrice')
  if 'qtyAvailable' in request.json:
    product.qty_available = request.json.get('qtyAvailable')

  db.session.commit()

  return jsonify({'success': True, 'message': 'Product updated'})


@admin_bp.route('/products/<int:product_id>', methods=['DELETE'])
@login_required('admin')
def delete_product(payload, product_id):
  product = Product.query.filter_by(id=product_id).first()

  if not product:
    return jsonify({'success': False, 'message': 'Product not found'}), 404

  # Check if product is referenced in any order
  if OrderItem.query.filter_by(product_id=product_id).first():
    return jsonify({'success': False, 'message': 'Cannot delete product with existing orders'}), 400

  db.session.delete(product)
  db.session.commit()

  return jsonify({'success': True, 'message': 'Product deleted'})


# ========== CUSTOMERS ==========

@admin_bp.route('/customers', methods=['GET'])
@login_required('admin')
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


@admin_bp.route('/customers', methods=['POST'])
@login_required('admin')
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


@admin_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
@login_required('admin')
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


# ========== SUPPLIERS ==========

@admin_bp.route('/suppliers', methods=['GET'])
@login_required('admin')
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


@admin_bp.route('/suppliers', methods=['POST'])
@login_required('admin')
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


@admin_bp.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
@login_required('admin')
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
