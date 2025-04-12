from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.stock import Stock
from schemas.stock import StockCreate, StockOut

def create_stock_view(stock: StockCreate, db: Session):
    db_stock = Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def read_stocks_view(db: Session):
    return db.query(Stock).all()

def update_stock_view(stock_id: int, stock_update: StockCreate, db: Session):
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    for key, value in stock_update.dict().items():
        setattr(stock, key, value)
    db.commit()
    db.refresh(stock)
    return stock

def delete_stock_view(stock_id: int, db: Session):
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    db.delete(stock)
    db.commit()
    return {"detail": "Stock deleted"}