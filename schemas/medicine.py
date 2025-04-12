from pydantic import BaseModel
from utils.mfd_exp import mfd, exp

class MedicineCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    mfd: str = mfd()
    exp: str = exp(mfd)

class MedicineOut(MedicineCreate):
    id: int

    class Config:
        orm_mode = True
