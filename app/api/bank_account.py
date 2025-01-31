from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.security import security
from app.schema import AccountCreate, AccountResponse
from app.service import bank_account_service
from app.service.bank_account import BankAccountService

router = APIRouter(
    prefix="/bank_account",
    tags=["Аккаунты"]
)


@router.post("", dependencies=[Depends(security.access_token_required)])
def create_account(
        user_id: int,
        object: AccountCreate,
        db: Session = Depends(get_db)
):
    result = bank_account_service.create_account_secure(user_id, object, db)
    return result

@router.get("", response_model=List[AccountResponse], dependencies=[Depends(security.access_token_required)])
def get_accounts( user_id: int, db: Session = Depends(get_db)):
    bank_account_service = BankAccountService()
    return bank_account_service.get_bank_accounts(db=db, user_id=user_id)

@router.delete("/{account_id}", dependencies=[Depends(security.access_token_required)])
def delete_account(account_id: int, db: Session = Depends(get_db)):
    return bank_account_service.delete_account(account_id, db)
