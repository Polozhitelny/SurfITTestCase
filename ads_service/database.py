from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создаем подключение к базе данных
database_url = "postgresql://postgres:12345@localhost/surfit"
engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
