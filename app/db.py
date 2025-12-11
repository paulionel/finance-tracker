from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in .env")

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    # Import models here to make sure they are registered
    from app.models import User, PaymentMethod, Category, Transaction, create_default_data
    
    # Create all tables
    SQLModel.metadata.create_all(engine)
    print("Database tables created!")
    
    # Populate default users, payment methods, categories
    create_default_data(engine)
