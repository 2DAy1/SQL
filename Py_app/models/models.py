from sqlalchemy import select, Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy

# create models
db = SQLAlchemy()


class Group(db.Model):
    __tablename__ = 'group'

    group_id = db.Column('group_id', db.Integer, primary_key=True)
    group_name = db.Column('group_name', db.String)

    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name

    def __repr__(self):
        return f'({self.group_id}) ({self.group_name})'

    def to_dict(self):
        return {'id': self.group_id, 'name': self.group_name}


class Course(db.Model):
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

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'group': self.group.to_dict(),
                'courses': [course.to_dict() for course in self.courses]}


class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column('student_id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(100))
    last_name = db.Column('last_name', db.String(100))
    group_id = db.Column(db.Integer, ForeignKey('group_id'))
    group = db.relationship('Group', backref=db.backref('students', lazy=True))
    courses = db.relationship('Course', secondary='student_courses', lazy='subquery',
                              backref=db.backref('students', lazy=True))

    def __init__(self, student_id, group_id, first_name, last_name, group, courses):
        self.student_id = student_id
        self.group_id = group_id
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.courses = courses

    def __repr__(self):
        return f'{self.student_id} {self.group_id} {self.first_name, self.last_name}'

    def to_dict(self):
        return {'id': self.student_id, 'name': self.name, 'group': self.group.to_dict(),
                'courses': [course.to_dict() for course in self.courses]}


# Define relationship between Student and Course models
student_courses = db.Table('student_courses',
                           db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
                           db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
                           )
