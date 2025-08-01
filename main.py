from fastapi import FastAPI, Query, Cookie, Path, HTTPException
from models import Transaction, Account, Authentication, TransactionResponse
from enum import Enum
from pydantic import BaseModel
from typing import Annotated
from database import Database, TransactionRepository, AccountRepository

app = FastAPI()
db = Database()

items = []


@app.post("/items")
def add_item(item : str):
    items.append(item)
    return items


@app.post("/Transaction", response_model=Transaction)
def transaction(transaction: Transaction):
    transaction_response = TransactionResponse(
        True,
        transaction.TransactionId,
        transaction.SenderId,
        transaction.RecipientId,
        transaction.Amount,
        transaction.Category,
        transaction.Reference
    )


@app.get("/account/{account_id}")
def get_account(account_id : int):
    return account_id


@app.post("/register")
def register(account: Account):
    return db.account.create_account(account)


@app.get("/login")
def login(account: Account):
    return db.account.auth_account(account)


@app.get("/items/{item_id}")
def get_item(item_id: Annotated[int, Path(gt=-1)]):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")