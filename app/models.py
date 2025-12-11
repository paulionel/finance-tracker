from sqlmodel import SQLModel, Field, Session, create_engine
from typing import Optional
from datetime import datetime

# -----------------------------
# Models
# -----------------------------

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # e.g., "Me", "Wife"


class PaymentMethod(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # e.g., "Cash", "Visa Card", "MasterCard"


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # e.g., "Grocery", "Mortgage", "Utilities"


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    payment_method_id: int = Field(foreign_key="paymentmethod.id")
    category_id: int = Field(foreign_key="category.id")
    amount: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    is_deposit: bool = False  # True if deposit/reimbursement
    note: Optional[str] = None  # optional extra info

# -----------------------------
# Example Default Data
# -----------------------------

def create_default_data(engine):
    with Session(engine) as session:
        # Users
        for name in ["Me", "Wife"]:
            if not session.query(User).filter_by(name=name).first():
                session.add(User(name=name))
        
        # Payment Methods
        for pm in ["Cash", "Visa Card", "MasterCard", "Debit Card"]:
            if not session.query(PaymentMethod).filter_by(name=pm).first():
                session.add(PaymentMethod(name=pm))
        
        # Categories
        for cat in ["Grocery", "Mortgage", "Utilities", "Entertainment", "Dining", "Other"]:
            if not session.query(Category).filter_by(name=cat).first():
                session.add(Category(name=cat))
        
        session.commit()
        print("Default users, payment methods, and categories added!")

