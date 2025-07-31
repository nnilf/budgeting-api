from fastapi import FastAPI
from models import Account

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/accounts/{account_id}")
def update_item(account_id: int, account: Account):
    return {"item_name": account.id, "account_id": account_id}