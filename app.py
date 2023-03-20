from create_db import create_db, run
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

    create_db(app, engine)

    from api import create_api
    create_api(app)

    return app




if __name__ == '__main__':
    create_app().run(debug=True)


