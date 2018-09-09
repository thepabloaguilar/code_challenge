from sqlalchemy import Column, Integer, String, DateTime
from . import PostgresBase

class User(PostgresBase):
    __tablename__ = 'user_login'

    _id = Column('id', Integer, primary_key=True)
    username = Column('username', String)
    password = Column('password', String)
    creation_date = Column('creation_date', DateTime)
