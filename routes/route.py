from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from models.model import Medicine
from schemas.schema import MedicineCreate, MedicineOut

router = APIRouter()

@router.post("/", response_model=MedicineOut)
def create_medicine(med: MedicineCreate, db: Session = Depends(get_db)):
    db_med = Medicine(**med.dict())
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med

@router.get("/", response_model=list[MedicineOut])
def read_medicines(db: Session = Depends(get_db)):
    return db.query(Medicine).all()

@router.get("/{medicine_id}", response_model=MedicineOut)
def read_medicine(medicine_id: int, db: Session = Depends(get_db)):
    med = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return med

@router.put("/{medicine_id}", response_model=MedicineOut)
def update_medicine(medicine_id: int, med_update: MedicineCreate, db: Session = Depends(get_db)):
    med = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    for key, value in med_update.dict().items():
        setattr(med, key, value)
    db.commit()
    db.refresh(med)
    return med

@router.delete("/{medicine_id}")
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    med = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    db.delete(med)
    db.commit()
    return {"detail": "Medicine deleted"}
