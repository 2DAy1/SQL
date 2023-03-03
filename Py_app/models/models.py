from sqlalchemy import select, Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy

# create models
db = SQLAlchemy()


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column('group_name', db.String)

    def __init__(self, id, group_name):
        self.id = id
        self.group_name = group_name

    def __repr__(self):
        return f'({self.id}) ({self.group_name})'

    def to_dict(self):
        return {'id': self.id, 'name': self.group_name}


class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column('course_name', db.String(100))
    description = db.Column('description', db.String(200))

    def __init__(self, id, course_name, description):
        self.id = id
        self.course_name = course_name
        self.description = description

    def __repr__(self):
        return f'{self.id} {self.course_name} {self.description}'

    def to_dict(self):
        return {'id': self.id, 'name': self.course_name, 'group': self.group.to_dict(),
                'courses': [course.to_dict() for course in self.courses]}


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(100))
    last_name = db.Column('last_name', db.String(100))
    group_id = db.Column(db.Integer, ForeignKey('group.id'))
    group = db.relationship('Group', backref=db.backref('students', lazy=True))
    courses = db.relationship('Course', secondary='student_courses', lazy='subquery',
                              backref=db.backref('students', lazy=True))

    def __init__(self, id, group_id, first_name, last_name, group, courses):
        self.id = id
        self.group_id = group_id
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.courses = courses

    def __repr__(self):
        return f'{self.id} {self.group_id} {self.first_name, self.last_name}'

    def to_dict(self):
        return {'id': self.id, 'first_name': self.first_name, 'last_name':self.last_name, 'group': self.group.to_dict(),
                'courses': [course.to_dict() for course in self.courses]}


# Define relationship between Student and Course models
student_courses = db.Table('student_courses',
                           db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
                           db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
                           )
