from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.model import Medicine
from schemas.schema import MedicineCreate, MedicineOut

def create_medicine_view(med: MedicineCreate, db: Session):
    db_med = Medicine(**med.dict())
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med

def read_medicines_view(db: Session):
    return db.query(Medicine).all()

def read_medicine_view(medicine_id: int, db: Session):
    med = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return med

def update_medicine_view(medicine_id: int, med_update: MedicineCreate, db: Session):
    med = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    for key, value in med_update.dict().items():
        setattr(med, key, value)
    db.commit()
    db.refresh(med)
    return med

def delete_medicine_view(medicine_id: int, db: Session):
    med = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    db.delete(med)
    db.commit()
    return {"detail": "Medicine deleted"}