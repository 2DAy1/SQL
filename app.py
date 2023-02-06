from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text, quoted_name
from flask import Flask, current_app
from config import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{user}:{password}@{host}:port/{db_name}'
app.config.from_object('config')
app.config.from_envvar('SQLALCHEMY_DATABASE_URI')
app.config.from_envvar('USER')
app.config.from_envvar('PASSWORD')
app.config.from_envvar('DB_NAME')

engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
if not database_exists(engine.url):
    create_database(engine.url)

db = SQLAlchemy(app)


class GroupModel(db.Model):
    id = Column('group_id', db.Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class StudentsModel(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group_id'))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    def __init__(self, group_id, first_name, last_name):
        self.group_id = group_id
        self.first_name = first_name
        self.last_name = last_name


class CourseModel(db.Model):
    id = db.Column('course_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

    def __init__(self, name, description):
        self.name = name
        self.description = description


db.create_all()




with engine.connect() as con:
    con.execute(f"CREATE USER {USER} WITH PASSWORD {PASSWORD}")
    con.execute(f"GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {USER}")





# if __name__ == '__main__':
#     create_app().run(debug=True)
