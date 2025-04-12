from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.stock import StockCreate, StockOut
from views.stock import (
    create_stock_view,
    read_stocks_view,
    update_stock_view,
    delete_stock_view
)

router = APIRouter()

@router.post("/", response_model=StockOut)
def create_stock(stock: StockCreate, db: Session = Depends(get_db)):
    return create_stock_view(stock, db)

@router.get("/", response_model=list[StockOut])
def read_stocks(db: Session = Depends(get_db)):
    return read_stocks_view(db)

@router.put("/{stock_id}", response_model=StockOut)
def update_stock(stock_id: int, stock_update: StockCreate, db: Session = Depends(get_db)):
    return update_stock_view(stock_id, stock_update, db)

@router.delete("/{stock_id}")
def delete_stock(stock_id: int, db: Session = Depends(get_db)):
    return delete_stock_view(stock_id, db)

