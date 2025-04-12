from pydantic import BaseModel
from typing import List

class MedicineItem(BaseModel):
    name: str
    quantity: int

class OrderCreate(BaseModel):
    customer_name: str
    medicines: List[MedicineItem]
    order_date: str
    address: str
    total_price: float

class OrderOut(OrderCreate):
    id: int

    class Config:
        orm_mode = True
