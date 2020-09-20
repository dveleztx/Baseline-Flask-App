# Imports
import datetime
import sqlalchemy
from flask_login import UserMixin
# Custom Imports
from data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    username = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False, index=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    profile_image_url = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    last_login = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
