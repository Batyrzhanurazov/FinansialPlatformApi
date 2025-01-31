## 🚀 Financial Platform API

Financial Platform API — это сервис для управления пользователями, их учетными записями и транзакциями. Использует FastAPI, SQLAlchemy и AuthX для авторизации через JWT (куки).

📌 Функции

🔐 Регистрация и аутентификация пользователей (JWT + Cookies)
🏦 Создание и управление банковскими счетами
💸 Создание и просмотр транзакций
📄 Документация API автоматически генерируется через Swagger


## 🚀 Запуск через Docker

### 1. Установите зависимости:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Клонируйте репозиторий:
```bash
git clone https://github.com/Batyrzhanurazov/FinansialPlatformApi.git
cd FinansialPlatformApi
```

### 3. Запустите проект
```bash
docker-compose up --build
```

### 🔧 Основные команды
- Запуск миграций:
```bash
docker-compose exec backend alembic upgrade head
```
- Остановка контейнеров:
```bash
docker-compose down
```

### 📖 Документация API

После запуска, документацию можно найти по адресу:

Swagger UI: http://localhost:8000/docs