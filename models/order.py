from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    order_date = Column(String)
    address = Column(String)
    total_price = Column(Float)

    # Define the relationship to OrderMedicine in 1-to-many fashion, back_populates is used to link the two classes, 
    # cascade is set so that when an Order is deleted, all related OrderMedicines are also deleted.
    # The delete-orphan option ensures that if an OrderMedicine is removed from the Order, it will be deleted from the database.
    medicines = relationship("OrderMedicine", back_populates="order", cascade="all, delete-orphan")


class OrderMedicine(Base):
    __tablename__ = "order_medicines"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    name = Column(String, index=True)
    quantity = Column(Integer)

    order = relationship("Order", back_populates="medicines")