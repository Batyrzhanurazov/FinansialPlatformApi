from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.models import Transaction
from app.service import transaction_service
from app.schema import TransactionCreate, TransactionResponse
from app.security import security

router = APIRouter(
    prefix="/transaction",
    tags=["Транзакции"]
)

@router.post("", dependencies=[Depends(security.access_token_required)])
def create_transaction(
        object: TransactionCreate,
        db: Session = Depends(get_db)
):
    result = transaction_service.create_transaction(db=db, object=object)
    return result


@router.get("/{user_id}/history", response_model=List[TransactionResponse])
def get_transaction_history(user_id: int, db: Session = Depends(get_db)):
    query = db.query(Transaction).filter(
        or_(Transaction.from_account_id == user_id, Transaction.to_account_id == user_id)
    )

    transactions = query.all()

    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this user")

    return transactions