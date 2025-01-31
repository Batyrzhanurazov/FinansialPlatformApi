from pydantic import BaseModel

class AccountCreate(BaseModel):
    currency: str = "USD"
    balance: float = 0.0

    class Config:
        orm_mode = True




class AccountResponse(BaseModel):
    bank_account_id: int
    currency: str
    balance: float
    user_id: int
    class Config:
        orm_mode = True
