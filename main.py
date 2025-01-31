from fastapi import FastAPI
from app.api.users import router as users_router
from app.api.bank_account import router as account_router
from app.api.transaction import router as transaction_router
from app.db.database import create_table, drop_table

drop_table()
create_table()
app = FastAPI()
app.include_router(users_router)
app.include_router(account_router)
app.include_router(transaction_router)