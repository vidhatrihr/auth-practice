from flask import Flask
from flask_cors import CORS
from models import db
from populate_db import populate_db

# Auth blueprint
from routes.auth import auth_bp

# Resource-based blueprints
from routes.products import products_bp
from routes.customers import customers_bp
from routes.suppliers import suppliers_bp
from routes.orders import orders_bp

# Role-specific blueprints (for truly role-specific routes)
from routes.admin import admin_bp
from routes.manager import manager_bp

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Register auth blueprint
app.register_blueprint(auth_bp)

# Register resource-based blueprints
app.register_blueprint(products_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(suppliers_bp)
app.register_blueprint(orders_bp)

# Register role-specific blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(manager_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

with app.app_context():
  db.create_all()
  populate_db()

app.run(debug=True)
