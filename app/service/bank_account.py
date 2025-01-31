from fastapi import HTTPException
from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.models.models import BankAccount
from app.schema import AccountCreate
from app.crud import bank_account_db

class BankAccountService:
    def create_account_secure(self, user_id: int, object: AccountCreate, db: Session):
        obj_in_data = jsonable_encoder(object)
        obj_in_data["user_id"] = user_id
        result = bank_account_db.create_account(db=db, object=obj_in_data)
        return result

    def create_account_registration(self,user_id: int, db: Session, object: AccountCreate):
        obj_in_data = jsonable_encoder(object)
        obj_in_data["user_id"] = user_id
        result = bank_account_db.create_account(db=db, object=obj_in_data)
        return result


    def get_bank_accounts(self, db: Session, user_id: int) -> List[BankAccount]:
        return db.query(BankAccount).filter(BankAccount.user_id == user_id).all()

    def delete_account(self, account_id: int, db: Session):
        account = bank_account_db.delete_account(db, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return {"detail": "Account successfully deleted"}


bank_account_service = BankAccountService()