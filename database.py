import sqlite3
import bcrypt
from fastapi import HTTPException
from models import Account

DB_NAME = "bank.db"


class TransactionRepository:

    def __init__(self, db):
            self.db = db

    def create_transaction():
        pass

    def get_transaction_by_account(account_id):
        pass


class AccountRepository:
        
        def __init__(self, db):
            self.db = db

        def create_account(self, account: Account):
            self.db.cursor.execute("SELECT 1 FROM accounts WHERE name = ?", (account.Name,))
            if self.db.cursor.fetchone():
                raise HTTPException(status_code=400, detail="Username already exists")
            
            # Hash password and insert new account
            hashed_pw = bcrypt.hashpw(account.Password.encode(), bcrypt.gensalt())

            self.db.cursor.execute("""
                INSERT INTO accounts (name, password)
                VALUES (?, ?)
            """, (account.Name, hashed_pw))

            self.db.conn.commit()
            account_id = self.db.cursor.lastrowid

            return {"message": "Account created", "accountId": account_id}


        def auth_account(self, account: Account):
            self.db.cursor.execute(
                "SELECT password FROM accounts WHERE name = ?", (account.Name,)
            )
            row = self.db.cursor.fetchone()

            if row:
                stored_hashed_password = row[0]
                if isinstance(stored_hashed_password, str):
                    stored_hashed_password = stored_hashed_password.encode() 

                if bcrypt.checkpw(account.Password.encode(), stored_hashed_password):
                    return {"message": "Login successful"}
                else:
                    raise HTTPException(status_code=401, detail="Invalid password")
            else:
                raise HTTPException(status_code=401, detail="Invalid username")

        def check_balance():
            pass

        def update_balance():
            pass


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_account_table()
        self.create_transaction_table()
        self.conn.commit()
        self.transaction = TransactionRepository(self)
        self.account = AccountRepository(self)
        print("✅ Database connection established and tables created.")


    def create_account_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                accountId INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                balance REAL NOT NULL DEFAULT 0.0
            );
        """)

    def create_transaction_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                TransactionId INTEGER PRIMARY KEY AUTOINCREMENT,
                SenderId INTEGER NOT NULL,
                RecipientId INTEGER NOT NULL,
                Amount REAL NOT NULL CHECK (Amount > 0.0),
                Category TEXT NOT NULL DEFAULT 'Transfer',
                Reference TEXT,
                FOREIGN KEY (SenderId) REFERENCES accounts(accountId),
                FOREIGN KEY (RecipientId) REFERENCES accounts(accountId)
            );
        """)

    def post(self):
        self.cursor.execute("""

        """)

    def get(self):
        self.cursor.execute("""

        """)

    def put(self):
        self.cursor.execute("""

        """)

    def delete(self):
        self.cursor.execute("""

        """)

    def close(self):
        self.conn.close()
        print("🔒 Database connection closed.")