from fastapi import FastAPI, Query, Cookie, Path, HTTPException
from models import Transaction, Account, Authentication
from enum import Enum
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

items = []


@app.post("/items")
def add_item(item : str):
    items.append(item)
    return items


@app.get("/items/{item_id}")
def get_item(item_id: Annotated[int, Path(gt=-1)]):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")