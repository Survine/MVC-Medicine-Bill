from pydantic import BaseModel

class MedicineCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    mfd: str
    exp: str

class MedicineOut(MedicineCreate):
    id: int

    class Config:
        orm_mode = True
