from sqlalchemy_utils import database_exists, create_database
from create_db.create_data import create_all_tables
from create_db.models import db
import click
from flask.cli import with_appcontext
from flask import current_app


def create_db_with_user(engine):
    # Check if the database exists, and create it if it does not
    if not database_exists(engine.url):
        create_database(engine.url)
        print("Database created successfully........")
    else:
        print("Database already exists")

    with engine.connect() as conn:
        try:
            conn.execute(f"CREATE USER {current_app.config['USER']} "
                         f"WITH PASSWORD '{current_app.config['PASSWORD']}';")
        except:
            print(f"this {current_app.config['USER']} exists")
        conn.execute(f"GRANT ALL PRIVILEGES ON DATABASE {current_app.config['DB_NAME']} "
                     f"TO {current_app.config['USER']};")
        print(f"{current_app.config['USER']} created successfully and granted all privileges "
              f"on {current_app.config['DB_NAME']}")


def db_init(app):
    db.init_app(app)


@click.command(name='run')
def run():
    db.create_all()
    click.echo('Database tables created!')

    with db.session.begin():
        create_all_tables()
        click.echo('Database get data')




def create_db(app, engine):
    db_init(app)

    with app.app_context():
        create_db_with_user(engine)
        # run()
    app.cli.command(run)
