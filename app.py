import asyncio
import httpx

account = "monzo"
amount = 42.0
category = "salary"

payload = {
    'account': account,
    'amount': amount,
    'category': category
}

async def get_transaction():
    async with httpx.AsyncClient() as client:
        r = await client.get('http://127.0.0.1:8000/items/5?q=somequery')
        print("Transaction response:", r.text)

async def get_user(account_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://127.0.0.1:8000/account/{account_id}')
        return response.json()

async def main():
    await get_transaction()
    user = await get_user(1)
    print("User data:", user)

# Run it
asyncio.run(main())