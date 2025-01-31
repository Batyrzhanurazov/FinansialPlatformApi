from datetime import datetime

from sqlalchemy.orm import Session
from app.schema import TransactionCreate
from app.models.models import Transaction


class TransactionDb:
    def create_transaction(self, db: Session, object: TransactionCreate):
        if isinstance(object.get('timestamp'), str):
            object['timestamp'] = datetime.fromisoformat(object['timestamp'].replace('Z', '+00:00'))
        db_object = Transaction(**object)
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object


transaction_db = TransactionDb()