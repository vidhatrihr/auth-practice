from flask import Flask
from flask_cors import CORS
from models import db
from populate_db import populate_db

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.manager import manager_bp

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173', 'http://localhost:5174',
     'http://127.0.0.1:5173', 'http://127.0.0.1:5174'])
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(manager_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

with app.app_context():
  db.create_all()
  populate_db()

app.run(debug=True)
