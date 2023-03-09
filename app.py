import click
from Py_app import *
from create_db import create_db_with_user
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask.cli import with_appcontext


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()

    db.init_app(app)

    with app.app_context():
        create_db_with_user(engine)
    # get db
    app.cli.command(create)
    # include test data in db

    # create api with blueprint admin
    from api import create_api
    create_api(app)

    return app


@click.command(name='run')
@with_appcontext
def create():
    db.create_all()
    click.echo('Database tables created!')

    create_all_tables()
    click.echo('Database get data')

if __name__ == '__main__':
    create_app().run(debug=True)
