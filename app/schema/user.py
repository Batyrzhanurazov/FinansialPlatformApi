from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    password: str
    fullname: str
    email: str
    class Config:
        orm_mode = True



class UserResponse(BaseModel):
    user_id: int
    login: str
    fullname: str
    email: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    login: str
    password: str

class Token(BaseModel):
    access_token: str

