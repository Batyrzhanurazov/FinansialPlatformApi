from sqlalchemy.orm import Session
from app.schema import AccountCreate
from app.models.models import BankAccount


class BankAccountDb:
    def create_account(self, db: Session, object: AccountCreate):
        db_object = BankAccount(**object)
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object

    def delete_account(self, db: Session, account_id: int):
        db_object = db.query(BankAccount).filter(BankAccount.bank_account_id == account_id).first()
        if not db_object:
            return None
        db.delete(db_object)
        db.commit()
        return db_object
bank_account_db = BankAccountDb()