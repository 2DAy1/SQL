from sqlalchemy import select, Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import current_app

# tmp = SQLAlchemy(app)
from sqlalchemy.orm import declarative_base

db = SQLAlchemy()

class GroupModel(db.Model):
    __tablename__ = 'group'

    group_id = db.Column('group_id', db.Integer, primary_key=True)
    group_name = db.Column('group_name', db.String)

    def __init__(self,group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name

    def __repr__(self):
        return f'({self.group_id}) ({self.group_name})'


class StudentsModel(db.Model):
    __tablename__ = 'student'

    student_id = db.Column('student_id', db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, ForeignKey('group_id'))
    first_name = db.Column('first_name', db.String(100))
    last_name = db.Column('last_name', db.String(100))

    def __init__(self, student_id, group_id, first_name, last_name):
        self.student_id = student_id
        self.group_id = group_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.student_id} {self.group_id} {self.first_name, self.last_name}'


class CourseModel(db.Model):
    __tablename__ = 'course'

    course_id = db.Column('course_id', db.Integer, primary_key=True)
    course_name = db.Column('course_name', db.String(100))
    description = db.Column('description', db.String(200))

    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description

    def __repr__(self):
        return f'{self.course_id} {self.course_name} {self.description}'



