from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.stock import Stock


# Utility: Deduct stock by medicine name
def deduct_stock(db: Session, medicine_name: str, quantity: int):
    stock = db.query(Stock).filter(Stock.medicine_name == medicine_name).first()
    if not stock:
        raise HTTPException(status_code=404, detail=f"No stock found for {medicine_name}")
    if stock.quantity < quantity:
        raise HTTPException(status_code=400, detail=f"Not enough stock for {medicine_name}")
    stock.quantity -= quantity
    db.add(stock)


# Utility: Restore stock by medicine name
def restore_stock(db: Session, medicine_name: str, quantity: int):
    stock = db.query(Stock).filter(Stock.medicine_name == medicine_name).first()
    if stock:
        stock.quantity += quantity
        db.add(stock)