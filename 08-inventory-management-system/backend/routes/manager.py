from datetime import datetime
from flask import Blueprint, jsonify, request
from models import db, Order, OrderItem, Product
from decorators import login_required

manager_bp = Blueprint('manager', __name__, url_prefix='/manager')


def serialize_order(order):
  return {
      'id': order.id,
      'type': order.type,
      'status': order.status,
      'dateCreated': order.date_created.isoformat() if order.date_created else None,
      'dateDelivered': order.date_delivered.isoformat() if order.date_delivered else None,
      'supplierId': order.supplier_id,
      'supplierName': order.supplier.name if order.supplier else None,
      'customerId': order.customer_id,
      'customerName': order.customer.name if order.customer else None,
      'items': [
          {
              'id': item.id,
              'productId': item.product_id,
              'productName': item.product.name if item.product else None,
              'qty': item.qty,
          }
          for item in order.items
      ]
  }


@manager_bp.route('/orders', methods=['GET'])
@login_required('manager')
def list_orders(payload):
  orders = Order.query.all()

  return jsonify({
      'success': True,
      'message': 'All orders fetched',
      'payload': {
          'orders': [serialize_order(order) for order in orders]
      }
  })


@manager_bp.route('/orders', methods=['POST'])
@login_required('manager')
def create_order(payload):
  order_type = request.json.get('type')  # incoming or outgoing
  supplier_id = request.json.get('supplierId')  # for incoming orders
  customer_id = request.json.get('customerId')  # for outgoing orders
  items = request.json.get('items', [])  # list of {productId, qty}

  order = Order(
      type=order_type,
      status='pending',
      supplier_id=supplier_id if order_type == 'incoming' else None,
      customer_id=customer_id if order_type == 'outgoing' else None,
  )
  db.session.add(order)
  db.session.flush()  # Get order ID before adding items

  for item in items:
    order_item = OrderItem(
        order_id=order.id,
        product_id=item.get('productId'),
        qty=item.get('qty'),
    )
    db.session.add(order_item)

  db.session.commit()

  return jsonify({
      'success': True,
      'message': 'Order created',
      'payload': {'orderId': order.id}
  })


@manager_bp.route('/orders/<int:order_id>', methods=['DELETE'])
@login_required('manager')
def delete_order(payload, order_id):
  order = Order.query.filter_by(id=order_id).first()

  if not order:
    return jsonify({'success': False, 'message': 'Order not found'}), 404

  if order.status != 'pending':
    return jsonify({'success': False, 'message': 'Only pending orders can be deleted'}), 400

  # Delete associated order items first
  OrderItem.query.filter_by(order_id=order_id).delete()
  db.session.delete(order)
  db.session.commit()

  return jsonify({'success': True, 'message': 'Order deleted'})


@manager_bp.route('/orders/<int:order_id>/deliver', methods=['PATCH'])
@login_required('manager')
def mark_order_delivered(payload, order_id):
  order = Order.query.filter_by(id=order_id).first()

  if not order:
    return jsonify({'success': False, 'message': 'Order not found'}), 404

  if order.status == 'delivered':
    return jsonify({'success': False, 'message': 'Order is already delivered'}), 400

  order.status = 'delivered'
  order.date_delivered = datetime.utcnow()
  db.session.commit()

  return jsonify({'success': True, 'message': 'Order marked as delivered'})
