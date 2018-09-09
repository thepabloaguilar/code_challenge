from sqlalchemy import Column, Integer, String, DateTime
from . import PostgresBase


class Customer(PostgresBase):
    __tablename__ = 'customer'

    _id = Column('id', Integer, primary_key=True)
    customer_name = Column('customer_name', String)
    customer_address = Column('customer_address', String)
    tax_id = Column('tax_id', String)
    gender = Column('gender', String(1))
    creation_date = Column('creation_date', DateTime)
