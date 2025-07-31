from fastapi import FastAPI, Body, Query
from models import Account
from enum import Enum
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Annotated[str | None, Query(max_length=50)] = None
    price: float
    tax: float | None = None


class Transaction(BaseModel):
    SenderId : int
    RecipientId : int
    Amount : float
    Category : Annotated[str, Body(max_length=50)] = 'Transfer'
    Reference : Annotated[str | None, Body(max_length=50)] = None


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/test/")
async def get_test(test: str, q: str | None = None):
    dictionary = {"query" : q, "test" : test}
    return dictionary