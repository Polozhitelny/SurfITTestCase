# Ad Service API

Ads Service API - это сервис по размещению объявлений. С помощью этого API пользователи могут регистрироваться, входить в систему, размещать объявления, просматривать список объявлений, удалять свои объявления, а также оставлять и удалять комментарии к объявлениям. API также предоставляет возможность администраторам удалять комментарии в любых объявлениях и назначать пользователям роль администратора.

## Требования

- Python 3.10
- Установленные зависимости из файла `requirements.txt`
- Сервер базы данных PostgreSQL

## Установка и запуск

1. Клонируйте репозиторий:

```shell
git clone https://github.com/your_username/ad-service-api.git
```

2. Установите зависимости:

```shell
pip install -r requirements.txt
```

3. Создайте базу данных PostgreSQL с именем ADS_SERVICE (или используйте другое имя) и настройте соединение с базой данных в файле main.py:

```shell
database_url = "postgresql://<ЛОГИН>:<ПАРОЛЬ>@localhost/<ИМЯ_БАЗЫ_ДАННЫХ>"
```

4. Запустите приложение:
```shell
uvicorn main:app --reload
```
## Документация API

После запуска приложения вы можете открыть документацию API, используя Swagger UI или ReDoc.

* Swagger UI: http://localhost:8000/docs
* ReDoc: http://localhost:8000/redoc

В документации API вы найдете описание всех доступных эндпоинтов, параметров запросов и ожидаемых ответов.
