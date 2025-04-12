from sqlalchemy import Column, Integer, String, Float
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    medicine_name = Column(String, index=True)
    quantity = Column(Integer)
    total_price = Column(Float)
    order_date = Column(String)
    andress = Column(String)