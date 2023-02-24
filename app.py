from pathlib import Path

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from views.admin import admin
    app.register_blueprint(admin)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
