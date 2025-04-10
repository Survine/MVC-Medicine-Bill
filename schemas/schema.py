from pydantic import BaseModel

class MedicineCreate(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool = True

class MedicineOut(MedicineCreate):
    id: int

    class Config:
        orm_mode = True
