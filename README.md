**Веб-приложение для изучения испанского языка**

Интерфейс:
- регистрация и авторизация пользователей
- статьи
- избранное
- словарь пользователя
- возможность редактировать профиль пользователя


**Запуск проекта** \
`chmod +x start.sh` \
`./start.sh `

**Пример .env:** \
`SECRET_KEY=key`  \
`MAIL=some_mail@mail.com` \
`PASSWORD=pass word pass word` \
`SQLALCHEMY_DATABASE_URI=postgresql://app:name@localhost:5436/db_name`

**Настройка базы данных** \
`docker run -d --name hispanist_project -p 5436:5432
 -v $HOME/DATABASES/hispanist_project:/var/lib/postresql/hispanist_project
 -e POSTGRES_PASSWORD=hispanist123
 -e POSTGRES_USER=app
 -e POSTGRES_DB=hispanist_db
 postgres`


`psql -h 127.0.0.1 -p 5436 -U app hispanist_db -f init_db.ddl
`
