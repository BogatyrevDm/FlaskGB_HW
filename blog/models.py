from blog.app import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
