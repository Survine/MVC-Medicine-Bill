from fastapi import FastAPI
from database import Base, engine
from routes import route

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register router
app.include_router(route.router, prefix="/medicines", tags=["Medicines"])
