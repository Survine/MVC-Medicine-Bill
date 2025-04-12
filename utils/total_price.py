from sqlalchemy.orm import Session
from schemas.order import MedicineItem
from models.medicine import Medicine


def calculate_total_price_from_db(medicines: list[MedicineItem], db: Session) -> float:
    total = 0.0
    for item in medicines:
        db_medicine = db.query(Medicine).filter(Medicine.name == item.name).first()
        if not db_medicine:
            raise ValueError(f"Medicine '{item.name}' not found in database")
        total += db_medicine.price * item.quantity
    return total