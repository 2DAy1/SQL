from sqlalchemy import select, Table, Column, Integer, String, MetaData, ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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


