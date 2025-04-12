from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    medicine_name = Column(String, index=True)
    quantity = Column(Integer, default=0)
    