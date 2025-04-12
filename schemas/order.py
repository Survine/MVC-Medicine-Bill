from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name: str
    medicine_name: list[str]
    quantity: int
    order_date: str
    address: str
    total_price: float

class OrderOut(OrderCreate):
    id: int
    
    class Config:
        orm_mode = True