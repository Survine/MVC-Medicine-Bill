from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.order import OrderCreate, OrderOut
from views.order import (
    create_order_view,
    read_orders_view,
    read_order_view,
    update_order_view,
    delete_order_view,
    read_orders_by_customer_view,
    read_orders_by_medicine_view
)

router = APIRouter()

@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order_view(order, db)

@router.get("/", response_model=list[OrderOut])
def read_orders(db: Session = Depends(get_db)):
    return read_orders_view(db)

@router.get("/{order_id}", response_model=OrderOut)
def read_order(order_id: int, db: Session = Depends(get_db)):
    return read_order_view(order_id, db)

@router.put("/{order_id}", response_model=OrderOut)
def update_order(order_id: int, order_update: OrderCreate, db: Session = Depends(get_db)):
    return update_order_view(order_id, order_update, db)

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return delete_order_view(order_id, db)

@router.get("/customer/{customer_name}", response_model=list[OrderOut])
def read_orders_by_customer(customer_name: str, db: Session = Depends(get_db)):
    return read_orders_by_customer_view(customer_name, db)

@router.get("/medicine/{medicine_name}", response_model=list[OrderOut])
def read_orders_by_medicine(medicine_name: str, db: Session = Depends(get_db)):
    return read_orders_by_medicine_view(medicine_name, db)