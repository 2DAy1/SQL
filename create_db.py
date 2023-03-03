from sqlalchemy_utils import database_exists, create_database

def create_db(engine):
    # Check if the database exists, and create it if it does not
    if not database_exists(engine.url):
        create_database(engine.url)
        print("Database created successfully........")
    else:
        print("Database already exists")