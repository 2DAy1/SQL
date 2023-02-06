HOST = "localhost"
USER = "user"
PASSWORD = "qwerty"
DB_NAME = "database"
SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:port/{DB_NAME}'
# SQLALCHEMY_DATABASE_URI = 'postgresql://user:qwerty@localhost:port/database'

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     DATABASE_URI = 'postgresql://:memory:'
#
#
# class ProductionConfig(Config):
#     DATABASE_URI = 'postgresql://user:qwerty@localhost:port/database'
#
#
# class TestingConfig(Config):
#     TESTING = True