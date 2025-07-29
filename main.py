from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Account(BaseModel):
    id: int
    name: str
    balance: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/accounts/{account_id}")
def update_item(account_id: int, account: Account):
    return {"item_name": account.id, "account_id": account_id}