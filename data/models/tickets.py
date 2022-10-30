from werkzeug.security import generate_password_hash, check_password_hash

import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'tickets'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    nft_id = sqlalchemy.Column(sqlalchemy.String)

    ticket = sqlalchemy.Column(sqlalchemy.LargeBinary)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
