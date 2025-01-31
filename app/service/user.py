from fastapi.encoders import jsonable_encoder
from app.schema import AccountCreate
from app.crud import user_db
from app.service.bank_account import bank_account_service
from sqlalchemy.orm import Session
from app.schema import UserCreate, UserLogin


class UserService:
    def register_user(self, object: UserCreate, db: Session):
        obj_in_data = jsonable_encoder(object)
        result = user_db.create_user(db= db, object= obj_in_data)

        user_id : int = result.user_id
        default_account = AccountCreate()
        bank_account_service.create_account_registration(user_id= user_id, object=default_account, db=db)
        return result

    def get_by_log_and_pass(self, object: UserLogin, db: Session):
        return user_db.get_by_log_and_pass(db= db, log= object.login, password= object.password)





user_service = UserService()
