import random

from sqlalchemy import select, Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# create models
db = SQLAlchemy()

# Define relationship between Student and Course models
student_course_table = db.Table('student_courses',
                                db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
                                db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
                                )

class GroupModel(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)

    students = db.relationship("StudentModel", back_populates="group")

    def __repr__(self):
        return f"<Group {self.name}>"

    def create(self):
        db.session.add(self)
        db.session.commit()

    def read(self):
        return GroupModel.query.filter_by(id=self.id).first()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)


class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(100))
    last_name = db.Column('last_name', db.String(100))
    group_id = db.Column(db.Integer, ForeignKey('group.id'))

    group = db.relationship("GroupModel", back_populates="students")
    courses = relationship("CourseModel", secondary=student_course_table, back_populates="students")

    def assign_random_courses(self, courses):
        num_courses = random.randint(1, 3)
        self.courses = random.sample(courses, num_courses)

    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name}>"

    def create(self):
        db.session.add(self)
        db.session.commit()

    def read(self):
        return StudentModel.query.filter_by(id=self.id).first()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class CourseModel(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    description = db.Column('description', db.String(200))

    students = db.relationship("StudentModel", secondary="student_course", back_populates="courses")

    def __repr__(self):
        return f"<Course {self.name}>"

    def create(self):
        db.session.add(self)
        db.session.commit()

    def read(self):
        return CourseModel.query.filter_by(id=self.id).first()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



