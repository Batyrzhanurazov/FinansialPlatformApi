﻿from authx import AuthXConfig

config = AuthXConfig()
config.JWT_SECRET_KEY = "your_secret_key"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_COOKIE_CSRF_PROTECT = False