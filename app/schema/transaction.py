from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: float
    currency: str
    type: str
    from_account_id: int = 0
    to_account_id: int
    transaction_type_id: int = 2
    timestamp: datetime


    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class TransactionResponse(BaseModel):
    amount: float
    currency: str
    type: str
    from_account_id: int
    to_account_id: int
    transaction_type_id: int
    timestamp: datetime
    transaction_id: int
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True