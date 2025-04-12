import os
from sqlalchemy import inspect
from database import engine, Base
from models.medicine import Medicine

# 🔥 Drop only the 'medicines' table
def drop_medicine_table():
    print("⚠️ Dropping 'medicines' table...")
    Medicine.__table__.drop(bind=engine)
    print("✅ 'medicines' table dropped.")

# 🧨 Delete entire SQLite database file
def delete_database():
    db_path = "medicines.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"🧨 Deleted database file: {db_path}")
    else:
        print(f"ℹ️ No database file found at {db_path}")

# 👀 View current tables in the connected database
def show_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    if tables:
        print("📋 Tables in the database:")
        for t in tables:
            print(f" - {t}")
    else:
        print("🚫 No tables found in the database.")

# === Run selected action here ===
if __name__ == "__main__":
    # Uncomment what you need to run:
    
    # drop_medicine_table()
    # delete_database()
    show_tables()
    pass
