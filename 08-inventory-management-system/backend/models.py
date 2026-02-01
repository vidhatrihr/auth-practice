"""
Relationship Pair   Parent Side         Child Side
User ↔ Session      User.sessions       Session.user
Product ↔ OrderItem Product.order_items OrderItem.product
Supplier ↔ Order    Supplier.orders     Order.supplier
Customer ↔ Order    Customer.orders     Order.customer
Order ↔ OrderItem   Order.items         OrderItem.order

Note: The parent side has a one-to-many relationship with the child side (one parent can have many children, but each child has only one parent).

The parent side uses uselist=True, as it refers to a list of child items.
The child side uses uselist=False, as it refers to a single parent item.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
  __tablename__ = 'users'
  id = Column(Integer, autoincrement=True, primary_key=True)
  name = Column(String)
  email = Column(String, unique=True)
  password = Column(String)
  role = Column(String)  # admin, manager

  sessions = relationship('Session', back_populates='user')


class Session(db.Model):
  __tablename__ = 'sessions'
  id = Column(Integer, autoincrement=True, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  date_created = Column(DateTime, default=datetime.utcnow)

  user = relationship('User', back_populates='sessions', uselist=False)


class Product(db.Model):
  __tablename__ = 'products'
  id = Column(Integer, autoincrement=True, primary_key=True)
  name = Column(String)
  cost_price = Column(Float)
  selling_price = Column(Float)
  qty_available = Column(Integer)

  order_items = relationship('OrderItem', back_populates='product')


class Supplier(db.Model):
  __tablename__ = 'suppliers'
  id = Column(Integer, autoincrement=True, primary_key=True)
  name = Column(String)

  orders = relationship('Order', back_populates='supplier')


class Customer(db.Model):
  __tablename__ = 'customers'
  id = Column(Integer, autoincrement=True, primary_key=True)
  name = Column(String)

  orders = relationship('Order', back_populates='customer')


class Order(db.Model):
  __tablename__ = 'orders'
  id = Column(Integer, autoincrement=True, primary_key=True)
  type = Column(String)  # incoming, outgoing
  date_created = Column(DateTime, default=datetime.utcnow)
  date_delivered = Column(DateTime, nullable=True)
  status = Column(String)  # pending, delivered
  supplier_id = Column(Integer, ForeignKey('suppliers.id'),
                       nullable=True)  # null for outgoing orders
  customer_id = Column(Integer, ForeignKey('customers.id'),
                       nullable=True)  # null for incoming orders

  supplier = relationship('Supplier', back_populates='orders', uselist=False)
  customer = relationship('Customer', back_populates='orders', uselist=False)
  items = relationship('OrderItem', back_populates='order')


class OrderItem(db.Model):
  __tablename__ = 'order_items'
  id = Column(Integer, autoincrement=True, primary_key=True)
  order_id = Column(Integer, ForeignKey('orders.id'))
  product_id = Column(Integer, ForeignKey('products.id'))
  qty = Column(Integer)

  order = relationship('Order', back_populates='items', uselist=False)
  product = relationship('Product', back_populates='order_items', uselist=False)
