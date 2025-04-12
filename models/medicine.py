from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    in_stock = Column(Boolean, default=True)
    mfd = Column(String)
    exp = Column(String)
