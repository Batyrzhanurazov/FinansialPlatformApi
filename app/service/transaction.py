from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.models.models import BankAccount, Transaction
from app.schema import TransactionCreate
from app.crud import transaction_db

CURRENCY_CONVERSION_RATES = {
    "USD": {
        "EUR": 0.85,
        "KZT": 450
    },
    "EUR": {
        "USD": 1 / 0.85,
        "KZT": 450 / 0.85
    },
    "KZT": {
        "USD": 1 / 450,
        "EUR": 1 / 450 * 0.85
    }
}


class TransactionService:
    def create_transaction(self, object: TransactionCreate, db: Session):
        if object.amount < 0 and object.type == "deposit":
            raise HTTPException(status_code=400, detail="Amount for deposit cannot be negative")
        if object.from_account_id == object.to_account_id:
            account = db.query(BankAccount).filter(BankAccount.bank_account_id == object.from_account_id).first()
            if not account:
                raise HTTPException(status_code=404, detail="Account not found")
            account.balance += object.amount
            db.commit()
            db.refresh(account)
            db_object = Transaction(**object.dict())
            db.add(db_object)
            db.commit()
            db.refresh(db_object)

            return db_object

        else:
            from_account = db.query(BankAccount).filter(BankAccount.bank_account_id == object.from_account_id).first()
            to_account = db.query(BankAccount).filter(BankAccount.bank_account_id == object.to_account_id).first()

            if not from_account:
                raise HTTPException(status_code=404, detail="Source account not found")
            if not to_account:
                raise HTTPException(status_code=404, detail="Target account not found")


            if from_account.balance < object.amount:
                raise HTTPException(status_code=400, detail="Insufficient funds")

            if from_account.currency != to_account.currency:
                converted_amount = CURRENCY_CONVERSION_RATES[from_account.currency].get(to_account.currency) * object.amount
                from_account.balance -= object.amount
                to_account.balance += converted_amount
            else:
                from_account.balance -= object.amount
                to_account.balance += object.amount


            db.commit()
            db.refresh(from_account)
            db.refresh(to_account)

            db_object = Transaction(**object.dict())
            db.add(db_object)
            db.commit()
            db.refresh(db_object)

            return db_object

transaction_service = TransactionService()
