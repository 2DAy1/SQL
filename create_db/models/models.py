from sqlalchemy import select, Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# create models
db = SQLAlchemy()

# Define relationship between Student and Course models


class GroupModel(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)

    students = db.relationship("StudentModel", back_populates="group")

    def __repr__(self):
        student_names = ",\n".join([f"{student.first_name} {student.last_name}" for student in self.students])
        return f"<Group {self.name}: {student_names}>"




class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(100))
    last_name = db.Column('last_name', db.String(100))
    group_id = db.Column(db.Integer, ForeignKey('groups.id'))

    group = db.relationship("GroupModel", uselist=False)
    courses = db.relationship("CourseModel", secondary='student_courses', back_populates="students")


    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name}>"




class CourseModel(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    description = db.Column('description', db.String(200))

    students = db.relationship("StudentModel", secondary="student_courses", back_populates="courses")

    def __repr__(self):
        return f"<Course {self.name}>"


student_courses = db.Table('student_courses',
                                db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
                                db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
                                )


