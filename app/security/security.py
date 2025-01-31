from authx import AuthX
from sqlalchemy.orm import Session

from app.models import User
from app.schema import UserLogin
from configs import config

security = AuthX(config= config)

class AppSecurity:
    def create_access_token(self, data: int):
        token = security.create_access_token(uid=str(data))
        return token

app_security = AppSecurity()