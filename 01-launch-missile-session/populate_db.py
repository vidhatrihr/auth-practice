from models import db, User
from werkzeug.security import generate_password_hash


def populate_db():
  if User.query.count() == 0:
    db.session.add(User(
        name='vidu',
        email='vidu@example.com',
        password=generate_password_hash('fish')
    ))
    db.session.commit()
