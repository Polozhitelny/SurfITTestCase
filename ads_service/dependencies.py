from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasicCredentials

from ads_service.security import pwd_context, security
from ads_service.database import SessionLocal
from ads_service.models import User


# Хелпер функция для получения текущей сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Получение текущего пользователя
def get_current_user(credentials: HTTPBasicCredentials = Depends(security), db=Depends(get_db)):
    user = db.query(User).filter(User.username == credentials.username).first()
    if not user or not pwd_context.verify(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user

# Проверка, является ли пользователь администратором
def is_admin(user: User):
    return user.is_admin
