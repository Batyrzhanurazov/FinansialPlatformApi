from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.models import Base, TransactionType

engine = create_engine('sqlite:///platform.db', echo=True)

session = sessionmaker(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()



def create_table():
    Base.metadata.create_all(engine)
    with session() as db:
        if db.query(TransactionType).count() == 0:
            db.add_all([
                TransactionType(transaction_name="Депозит", transaction_code="DEP"),
                TransactionType(transaction_name="Снятие средств", transaction_code="WIT"),
                TransactionType(transaction_name="Перевод", transaction_code="TRA")
            ])
            db.commit()

def drop_table():
    Base.metadata.drop_all(engine)