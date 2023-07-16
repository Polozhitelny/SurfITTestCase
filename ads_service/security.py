from fastapi.security import HTTPBasic
from passlib.context import CryptContext

# Создаем хэш-пароль для хранения в базе данных
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Создаем экземпляр HTTPBasic для аутентификации
security = HTTPBasic()
