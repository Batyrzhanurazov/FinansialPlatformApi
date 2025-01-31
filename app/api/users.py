from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service import user_service
from app.schema import UserCreate, UserResponse, Token, UserLogin
from configs import config
from app.security import app_security, security

router = APIRouter(
    prefix="/user",
    tags=["Клиенты"]
)

@router.post("/register", response_model=UserResponse)
def register_user(
        object : UserCreate,
        db : Session = Depends(get_db)
        ):
    result = user_service.register_user(db=db, object=object)
    return result


@router.post("/login", response_model=Token)
def login_user(user: UserLogin, response: Response, db: Session = Depends(get_db)):
    # Вход в систему
    db_user = user_service.get_by_log_and_pass(db=db, object=user)
    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )
    access_token = app_security.create_access_token(data = db_user.user_id)
    response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, access_token)
    return {"access_token": access_token}