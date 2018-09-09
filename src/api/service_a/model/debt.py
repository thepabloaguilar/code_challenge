from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from . import PostgresBase

class Debt(PostgresBase):
    __tablename__ = 'debt'

    _id = Column('id', Integer, primary_key=True)
    customer_id = Column('customer_id', Integer, ForeignKey('customer.id'))
    business_id = Column('business_id', Integer, ForeignKey('business.id'))
    description = Column('description', String)
    amount = Column('amount', Numeric(16, 6))
    payment_date = Column('payment_date', Date)
    expiry_date = Column('expiry_date', Date)
