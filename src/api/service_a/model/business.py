from sqlalchemy import Column, Integer, String
from . import PostgresBase


class Business(PostgresBase):
    __tablename__ = 'business'

    _id = Column('id', Integer, primary_key=True)
    business_name = Column('business_name', String)
