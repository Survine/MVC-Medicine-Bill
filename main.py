from fastapi import FastAPI
from database import Base, engine
from routes import medicine, order, stock

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register router
app.include_router(medicine.router, prefix="/medicines", tags=["Medicines"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
app.include_router(stock.router, prefix="/stocks", tags=["Stocks"])
