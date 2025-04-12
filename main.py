from fastapi import FastAPI
from database import Base, engine
from routes import medicine

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register router
app.include_router(medicine.router, prefix="/medicines", tags=["Medicines"])
