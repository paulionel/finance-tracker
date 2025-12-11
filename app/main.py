from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db import init_db
from app.models import Transaction, User, Category, PaymentMethod
from app.crud import (
    create_transaction, get_transaction, get_transactions, update_transaction, delete_transaction,
    create_user, get_user, get_users, update_user, delete_user,
    create_category, get_category, get_categories, update_category, delete_category,
    create_payment_method, get_payment_method, get_payment_methods, update_payment_method, delete_payment_method
)

app = FastAPI(title="Finance Tracker")

# Initialize database tables
@app.on_event("startup")
def on_startup():
    init_db()

# Serve static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve HTML templates
templates = Jinja2Templates(directory="templates")

# Root endpoint serving index.html
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# -----------------------------
# Transactions Endpoints
# -----------------------------
@app.post("/transactions/", response_model=Transaction)
def api_create_transaction(transaction: Transaction):
    return create_transaction(transaction)

@app.get("/transactions/", response_model=list[Transaction])
def api_get_transactions(skip: int = 0, limit: int = 100):
    return get_transactions(skip, limit)

@app.get("/transactions/{transaction_id}", response_model=Transaction)
def api_get_transaction(transaction_id: int):
    transaction = get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.put("/transactions/{transaction_id}", response_model=Transaction)
def api_update_transaction(transaction_id: int, transaction: Transaction):
    updated = update_transaction(transaction_id, **transaction.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated

@app.delete("/transactions/{transaction_id}")
def api_delete_transaction(transaction_id: int):
    if not delete_transaction(transaction_id):
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"ok": True}

# -----------------------------
# Users Endpoints
# -----------------------------
@app.post("/users/", response_model=User)
def api_create_user(user: User):
    return create_user(user)

@app.get("/users/", response_model=list[User])
def api_get_users(skip: int = 0, limit: int = 100):
    return get_users(skip, limit)

@app.get("/users/{user_id}", response_model=User)
def api_get_user(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
def api_update_user(user_id: int, user: User):
    updated = update_user(user_id, **user.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete("/users/{user_id}")
def api_delete_user(user_id: int):
    if not delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True}

# -----------------------------
# Categories Endpoints
# -----------------------------
@app.post("/categories/", response_model=Category)
def api_create_category(category: Category):
    return create_category(category)

@app.get("/categories/", response_model=list[Category])
def api_get_categories(skip: int = 0, limit: int = 100):
    return get_categories(skip, limit)

@app.get("/categories/{category_id}", response_model=Category)
def api_get_category(category_id: int):
    category = get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.put("/categories/{category_id}", response_model=Category)
def api_update_category(category_id: int, category: Category):
    updated = update_category(category_id, **category.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated

@app.delete("/categories/{category_id}")
def api_delete_category(category_id: int):
    if not delete_category(category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    return {"ok": True}

# -----------------------------
# Payment Methods Endpoints
# -----------------------------
@app.post("/payment-methods/", response_model=PaymentMethod)
def api_create_payment_method(payment_method: PaymentMethod):
    return create_payment_method(payment_method)

@app.get("/payment-methods/", response_model=list[PaymentMethod])
def api_get_payment_methods(skip: int = 0, limit: int = 100):
    return get_payment_methods(skip, limit)

@app.get("/payment-methods/{payment_method_id}", response_model=PaymentMethod)
def api_get_payment_method(payment_method_id: int):
    method = get_payment_method(payment_method_id)
    if not method:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return method

@app.put("/payment-methods/{payment_method_id}", response_model=PaymentMethod)
def api_update_payment_method(payment_method_id: int, payment_method: PaymentMethod):
    updated = update_payment_method(payment_method_id, **payment_method.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return updated

@app.delete("/payment-methods/{payment_method_id}")
def api_delete_payment_method(payment_method_id: int):
    if not delete_payment_method(payment_method_id):
        raise HTTPException(status_code=404, detail="Payment method not found")
    return {"ok": True}

