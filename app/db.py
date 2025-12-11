from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    # Create all tables defined in models
    SQLModel.metadata.create_all(engine)
    print("Database tables created!")

