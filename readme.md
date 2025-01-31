## 🚀 Financial Platform API

Financial Platform API — это сервис для управления пользователями, их учетными записями и транзакциями. Использует FastAPI, SQLAlchemy и AuthX для авторизации через JWT (куки).

📌 Функции

🔐 Регистрация и аутентификация пользователей (JWT + Cookies)
🏦 Создание и управление банковскими счетами
💸 Создание и просмотр транзакций
📄 Документация API автоматически генерируется через Swagger

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/Batyrzhanurazov/FinansialPlatformApi.git
cd FinansialPlatformApi
```

### 2. Установите зависимости:
- Python 3.10
- Pip
```bash
```bash
pip install -r requirements.txt
```
### 3. Запустите проект
```bash
uvicorn main:app --reload
```


### 📖 Документация API

После запуска, документацию можно найти по адресу:

Swagger UI: http://localhost:8000/docs