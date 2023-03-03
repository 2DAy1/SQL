from sqlalchemy_utils import database_exists, create_database


def create_db_with_user(self):
    # Check if the database exists, and create it if it does not
    if not database_exists(self.engine.url):
        create_database(self.engine.url)
        print("Database created successfully........")

        with self.engine.connect() as conn:
            conn.execute("CREATE USER myuser WITH PASSWORD 'mypassword';")
            conn.execute("GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;")
            print("User created successfully and granted all privileges on mydatabase")
    else:
        print("Database already exists")
