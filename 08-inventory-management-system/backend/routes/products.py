from flask import Blueprint, jsonify, request
from models import db, Product, OrderItem
from decorators import role_required

products_bp = Blueprint('products', __name__, url_prefix='/products')


@products_bp.route('', methods=['GET'])
@role_required(['admin', 'manager'])
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


@products_bp.route('', methods=['POST'])
@role_required('admin')
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


@products_bp.route('/<int:product_id>', methods=['PATCH'])
@role_required('admin')
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


@products_bp.route('/<int:product_id>', methods=['DELETE'])
@role_required('admin')
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
