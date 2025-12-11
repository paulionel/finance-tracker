from sqlmodel import Session, select
from app.models import Transaction, User, Category, PaymentMethod
from app.db import engine

# -----------------------------
# Transactions
# -----------------------------

def create_transaction(transaction: Transaction) -> Transaction:
    with Session(engine) as session:
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction

def get_transaction(transaction_id: int) -> Transaction | None:
    with Session(engine) as session:
        return session.get(Transaction, transaction_id)

def get_transactions(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        statement = select(Transaction).offset(skip).limit(limit)
        results = session.exec(statement)
        return results.all()

def update_transaction(transaction_id: int, **kwargs) -> Transaction | None:
    with Session(engine) as session:
        transaction = session.get(Transaction, transaction_id)
        if not transaction:
            return None
        for key, value in kwargs.items():
            setattr(transaction, key, value)
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction

def delete_transaction(transaction_id: int) -> bool:
    with Session(engine) as session:
        transaction = session.get(Transaction, transaction_id)
        if not transaction:
            return False
        session.delete(transaction)
        session.commit()
        return True

# -----------------------------
# Users
# -----------------------------

def create_user(user: User) -> User:
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def get_user(user_id: int) -> User | None:
    with Session(engine) as session:
        return session.get(User, user_id)

def get_users(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        statement = select(User).offset(skip).limit(limit)
        return session.exec(statement).all()

def update_user(user_id: int, **kwargs) -> User | None:
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            setattr(user, key, value)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def delete_user(user_id: int) -> bool:
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True

# -----------------------------
# Categories
# -----------------------------

def create_category(category: Category) -> Category:
    with Session(engine) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category

def get_category(category_id: int) -> Category | None:
    with Session(engine) as session:
        return session.get(Category, category_id)

def get_categories(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        statement = select(Category).offset(skip).limit(limit)
        return session.exec(statement).all()

def update_category(category_id: int, **kwargs) -> Category | None:
    with Session(engine) as session:
        category = session.get(Category, category_id)
        if not category:
            return None
        for key, value in kwargs.items():
            setattr(category, key, value)
        session.add(category)
        session.commit()
        session.refresh(category)
        return category

def delete_category(category_id: int) -> bool:
    with Session(engine) as session:
        category = session.get(Category, category_id)
        if not category:
            return False
        session.delete(category)
        session.commit()
        return True

# -----------------------------
# Payment Methods
# -----------------------------

def create_payment_method(payment_method: PaymentMethod) -> PaymentMethod:
    with Session(engine) as session:
        session.add(payment_method)
        session.commit()
        session.refresh(payment_method)
        return payment_method

def get_payment_method(payment_method_id: int) -> PaymentMethod | None:
    with Session(engine) as session:
        return session.get(PaymentMethod, payment_method_id)

def get_payment_methods(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        statement = select(PaymentMethod).offset(skip).limit(limit)
        return session.exec(statement).all()

def update_payment_method(payment_method_id: int, **kwargs) -> PaymentMethod | None:
    with Session(engine) as session:
        method = session.get(PaymentMethod, payment_method_id)
        if not method:
            return None
        for key, value in kwargs.items():
            setattr(method, key, value)
        session.add(method)
        session.commit()
        session.refresh(method)
        return method

def delete_payment_method(payment_method_id: int) -> bool:
    with Session(engine) as session:
        method = session.get(PaymentMethod, payment_method_id)
        if not method:
            return False
        session.delete(method)
        session.commit()
        return True

