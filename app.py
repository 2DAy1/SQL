from create_db import create_db_with_user
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()

    # get db
    from Py_app import db
    db.init_app(app)

    with app.app_context():
        create_db_with_user(engine)
        db.create_all()

    # include test data in db

    # create api with bluprint admin
    from api import create_api
    create_api(app)

    from views import admin
    app.register_blueprint(admin)

    return app



if __name__ == '__main__':
    create_app().run(debug=True)
