from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasicCredentials

from ads_service.dependencies import get_db, get_current_user
from ads_service.models import Ad, Comment, User
from ads_service.security import pwd_context
from main import app


# Регистрация нового пользователя
@app.post("/users")
def register_user(username: str, password: str, db=Depends(get_db)):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()
    return {"message": "User registered successfully"}


# Вход в систему
@app.post("/login")
def login(credentials: HTTPBasicCredentials, db=Depends(get_db)):
    user = db.query(User).filter(User.username == credentials.username).first()
    if not user or not pwd_context.verify(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Logged in successfully"}

# Создание объявления
@app.post("/ads")
def create_ad(title: str, description: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    ad = Ad(title=title, description=description, user_id=current_user.id)
    db.add(ad)
    db.commit()
    return {"message": "Ad created successfully"}


# Получение списка объявлений
@app.get("/ads")
def get_ads(db=Depends(get_db)):
    ads = db.query(Ad).all()
    return ads


# Просмотр одного объявления
@app.get("/ads/{ad_id}")
def get_ad(ad_id: int, db=Depends(get_db)):
    ad = db.query(Ad).filter(Ad.id == ad_id).first()
    if not ad:
        raise HTTPException(status_code=404, detail="Ad not found")
    return ad


# Удаление объявления
@app.delete("/ads/{ad_id}")
def delete_ad(ad_id: int, current_user=Depends(get_current_user), db=Depends(get_db)):
    ad = db.query(Ad).filter(Ad.id == ad_id, Ad.user_id == current_user.id).first()
    if not ad:
        raise HTTPException(status_code=404, detail="Ad not found")
    db.delete(ad)
    db.commit()
    return {"message": "Ad deleted successfully"}


# Удаление комментария
@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, current_user=Depends(get_current_user), db=Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    ad = db.query(Ad).filter(Ad.id == comment.ad_id).first()
    if not ad or (current_user.id != ad.user_id and not current_user.is_admin):
        raise HTTPException(status_code=403, detail="Unauthorized to delete the comment")
    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted successfully"}


# Назначение пользователя администратором
@app.post("/users/{user_id}/admin")
def assign_admin(user_id: int, current_user=Depends(get_current_user), db=Depends(get_db)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized to assign admin role")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_admin = True
    db.commit()
    return {"message": "User assigned admin role successfully"}
