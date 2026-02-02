from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()


class User(db.Model):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  email = Column(String)
  password = Column(String)


class Session(db.Model):
  __tablename__ = 'sessions'
  id = Column(Integer, primary_key=True, autoincrement=True)
  token = Column(String, unique=True)
  user_id = Column(Integer)
