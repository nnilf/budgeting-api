from pydantic import BaseModel
from typing import Annotated
from fastapi import Body, Cookie

class Account(BaseModel):
    AccountId : int
    Balance : float
    Name : str
    Password : str


class Transaction(BaseModel):
    TransactionId : int
    SenderId : int
    RecipientId : int
    Amount : Annotated[float, Body(gt=0.0)]
    Category : Annotated[str, Body(max_length=50)] = 'Transfer'
    Reference : Annotated[str | None, Body(max_length=50)] = None


class Authentication(BaseModel):
    Name : Annotated[str, Body(gt=0)]
    Password : Annotated[str, Body(gt=7)]


class Cookies(BaseModel):
    AccountId : int