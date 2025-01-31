from sqlalchemy.orm import Session
from app.schema import UserCreate
from app.models.models import  User


class UserDb:
    def create_user(self, db: Session, object: UserCreate):
        db_object = User(**object)
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object

    def get_by_log_and_pass(self, db: Session, log: str, password: str):
        result = db.query(User).filter(User.login == log, User.password == password).first()
        return result

user_db = UserDb()