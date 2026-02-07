import json
from models import db, User, Product, Supplier, Customer, Order, OrderItem
from werkzeug.security import generate_password_hash


def populate_db():
  if User.query.count() > 0:
    return

  # Create Users
  admin = User(
      email='admin@example.com',
      name='Admin User',
      password=generate_password_hash('password'),
      role='admin'
  )

  manager = User(
      email='manager@example.com',
      name='Manager User',
      password=generate_password_hash('password'),
      role='manager'
  )

  db.session.add_all([admin, manager])

  # Create Products from JSON
  with open('products.json') as f:
    product_data = json.load(f)

  products = [Product(**p) for p in product_data]

  db.session.add_all(products)

  # Create Suppliers
  suppliers = [
      Supplier(name='Supplier A'),
      Supplier(name='Supplier B')
  ]
  db.session.add_all(suppliers)

  # Create Customers
  customers = [
      Customer(name='Customer X'),
      Customer(name='Customer Y')
  ]
  db.session.add_all(customers)

  db.session.commit()

  # Create Incoming Order (Pending, 3 products)
  incoming_order = Order(
      type='incoming',
      status='pending',
      supplier_id=suppliers[0].id
  )

  incoming_items = [
      OrderItem(order=incoming_order, product_id=products[0].id, qty=10),
      OrderItem(order=incoming_order, product_id=products[1].id, qty=20),
      OrderItem(order=incoming_order, product_id=products[2].id, qty=30)
  ]

  db.session.add(incoming_order)
  db.session.add_all(incoming_items)

  # Create Outgoing Order (Pending, 2 products)
  outgoing_order = Order(
      type='outgoing',
      status='pending',
      customer_id=customers[0].id
  )

  outgoing_items = [
      OrderItem(order=outgoing_order, product_id=products[3].id, qty=5),
      OrderItem(order=outgoing_order, product_id=products[4].id, qty=5)
  ]

  db.session.add(outgoing_order)
  db.session.add_all(outgoing_items)

  db.session.commit()
