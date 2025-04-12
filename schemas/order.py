from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class MedicineItem(BaseModel):
    name: str
    quantity: int

class OrderCreate(BaseModel):
    customer_name: str
    medicines: List[MedicineItem]
    order_date: str = Field(default_factory=lambda: datetime.now().strftime("%d-%m-%Y"))
    address: str


class OrderOut(OrderCreate):
    id: int
    total_price: float

    class Config:
        orm_mode = True
