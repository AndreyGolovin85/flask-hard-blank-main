# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db


# функция создания основного объекта app
from views.director import director_ns
from views.genre import genres_ns
from views.movie import movies_ns


def create_app(config_object):
    appliction = Flask(__name__)
    appliction.config.from_object(config_object)
    register_extensions(appliction)
    return appliction


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(director_ns)


app = create_app(Config)

if __name__ == '__main__':
    app.run(port=5001)
