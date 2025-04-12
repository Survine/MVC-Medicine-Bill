from  pydantic import BaseModel

class StockCreate(BaseModel):
    medicine_name: str
    quantity: int

class StockOut(StockCreate):
    id: int

    class Config:
        orm_mode = True