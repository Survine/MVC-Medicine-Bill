from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.order import Order
from schemas.order import OrderCreate, OrderOut

def create_order_view(order: OrderCreate, db: Session):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def read_orders_view(db: Session):
    return db.query(Order).all()

def read_order_view(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

def update_order_view(order_id: int, order_update: OrderCreate, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    for key, value in order_update.dict().items():
        setattr(order, key, value)
    db.commit()
    db.refresh(order)
    return order

def delete_order_view(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"detail": "Order deleted"}

def read_orders_by_customer_view(customer_name: str, db: Session):
    orders = db.query(Order).filter(Order.customer_name == customer_name).all()
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this customer")
    return orders

def read_orders_by_medicine_view(medicine_name: str, db: Session):
    orders = db.query(Order).filter(Order.medicine_name == medicine_name).all()
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this medicine")
    return orders

