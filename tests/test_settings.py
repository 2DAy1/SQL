DB = "postgresql"
USER = "postgres"
PASSWORD = "davdad2002"
HOST = "localhost"
DB_NAME = "test_db"
SECRET_KEY = '321412214124fsdsafash0i8hf32yrnydc8payd8r31q08'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = f"{DB}://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"
