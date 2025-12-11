from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in .env")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session
)

def init_db():
    # Import models here to make sure they are registered
    from app.models import User, PaymentMethod, Category, Transaction, create_default_data
    
    # Create all tables
    SQLModel.metadata.create_all(engine)
    print("Database tables created!")
    
    # Populate default users, payment methods, categories
    create_default_data(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
