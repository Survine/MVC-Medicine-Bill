from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.schema import MedicineCreate, MedicineOut
from views.view import (
    create_medicine_view,
    read_medicines_view,
    read_medicine_view,
    update_medicine_view,
    delete_medicine_view
)

router = APIRouter()

@router.post("/", response_model=MedicineOut)
def create_medicine(med: MedicineCreate, db: Session = Depends(get_db)):
    return create_medicine_view(med, db)

@router.get("/", response_model=list[MedicineOut])
def read_medicines(db: Session = Depends(get_db)):
    return read_medicines_view(db)

@router.get("/{medicine_id}", response_model=MedicineOut)
def read_medicine(medicine_id: int, db: Session = Depends(get_db)):
    return read_medicine_view(medicine_id, db)

@router.put("/{medicine_id}", response_model=MedicineOut)
def update_medicine(medicine_id: int, med_update: MedicineCreate, db: Session = Depends(get_db)):
    return update_medicine_view(medicine_id, med_update, db)

@router.delete("/{medicine_id}")
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    return delete_medicine_view(medicine_id, db)