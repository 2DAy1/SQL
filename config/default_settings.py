DB = "postgresql"
USER = "user"
PASSWORD = "qwerty"
HOST = "127.0.0.1:5000"
DB_NAME = "appdb"
SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# TEST_SETTINGS = dict(DB="postgresql", USER="test_user", PASSWORD="1234", HOST="localhost", DB_NAME="test_db.tmp")

SQLALCHEMY_DATABASE_URI = f"{DB}://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"
SQLALCHEMY_DATABASE_URI1 = 'postgresql://username:password@localhost/mydatabase'
