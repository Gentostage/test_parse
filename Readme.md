# Как развернуть проект

## Docker 

```bash
    # Создать и запустить контейнер
    $ docker-compose up --build
    # Создать миграцию 
    $ docker-compose run web python manage.py migrate
    # Спарсить сайт 
    $ docker-compose run web python manage.py parse

```

## Локально
### Требования 
python 3.7, mysql:5.7
Обязательно поменяйте настройки подключения к базе данные в файле `config/settings.py`

```bash
    # Установка pipenv 
    $ pip install pipenv
    # Установка зависимостей
    $ pipenv install
    # Активировать виртуальное окружение 
    $ pipenv shell
    # Выполнить миграцию
    $ python manage.py migrate
    # Запустить парсер 
    $ python manage.py parse
    # Запустить django сервер
    $ python manage.py runserver
```
