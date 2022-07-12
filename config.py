# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.
import os

DATABASE = os.path.join("data/movies.db")


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = "localhost"
    PORT = 2331