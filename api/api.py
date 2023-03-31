import json
from flask_restful import Api
from flask import jsonify, make_response, config, current_app, Blueprint
from flask_restful import Resource, request, marshal_with, fields
from create_db import db, StudentModel, GroupModel, CourseModel
from dicttoxml import dicttoxml
from flasgger import swag_from


studentFields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'group_id': fields.Integer
}

courseFields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String
}

groupeFields = {
    'id': fields.Integer,
    'name': fields.String,
}


class Students(Resource):
    @marshal_with(studentFields)
    def get(self):
        return StudentModel.query.all()

    @marshal_with(studentFields)
    def post(self):
        data = request.json
        student = StudentModel(
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        db.session.add(student)
        db.session.commit()

        return student, 201


class Student(Resource):
    @marshal_with(studentFields)
    def get(self, pk):
        student = StudentModel.query.filter_by(id=pk).first()
        if not student:
            return {'message': 'Student not found'}, 404
        return student

    @marshal_with(studentFields)
    def put(self, pk):
        student = StudentModel.query.filter_by(id=pk).first()
        if not student:
            return {'message': 'Student not found'}, 404
        data = request.json
        student.first_name = data.get('first_name', student.first_name)
        student.last_name = data.get('last_name', student.last_name)
        student.group_id = data.get('group_id', student.group_id)
        db.session.commit()
        return student

    @marshal_with(studentFields)
    def delete(self, pk):
        student = StudentModel.query.filter_by(id=pk).first()
        if not student:
            return {'message': 'Student not found'}, 404
        db.session.delete(student)
        db.session.commit()
        return student, 204


class Groups(Resource):
    @marshal_with(groupeFields)
    def get(self):
        return GroupModel.query.all()

    @marshal_with(groupeFields)
    def post(self):
        data = request.json
        group = GroupModel(
            name=data['name'],

        )
        db.session.add(group)
        db.session.commit()

        return group, 201



class Group(Resource):
    @marshal_with(groupeFields)
    def get(self, pk):
        group = GroupModel.query.filter_by(id=pk).first()
        if not group:
            return {'message': 'Group not found'}, 404
        return group

    @marshal_with(groupeFields)
    def put(self, pk):
        group = GroupModel.query.filter_by(id=pk).first()
        if not group:
            return {'message': 'Group not found'}, 404
        data = request.json
        group.name = data.get('name', group.name)
        db.session.commit()
        return group

    @marshal_with(groupeFields)
    def delete(self, pk):
        group = GroupModel.query.filter_by(id=pk).first()
        if not group:
            return {'message': 'Group not found'}, 404
        db.session.delete(group)
        db.session.commit()
        return group, 204


class Courses(Resource):
    @marshal_with(courseFields)
    def get(self):
        return CourseModel.query.all()

    def post(self):
        data = request.json
        course = CourseModel(
            name=data['name'],
            description=data['description']
        )
        db.session.add(course)
        db.session.commit()

        return course, 201


class Course(Resource):
    @marshal_with(courseFields)
    def get(self, pk):
        return CourseModel.query.filter_by(id=pk).first()

    @marshal_with(courseFields)
    def put(self, pk):
        course = CourseModel.query.filter_by(id=pk).first()
        if not course:
            return {'message': 'Course not found'}, 404

        data = request.json
        if 'name' in data:
            course.name = data['name']
        if 'description' in data:
            course.description = data['description']

        db.session.commit()
        return course

    @marshal_with(courseFields)
    def delete(self, pk):
        course = CourseModel.query.filter_by(id=pk).first()
        if not course:
            return {'message': 'Course not found'}, 404

        db.session.delete(course)
        db.session.commit()
        return {'message': 'Course deleted'}, 200


class CourseStudents(Resource):
    @marshal_with(studentFields)
    def get(self, pk):
        course = CourseModel.query.filter_by(id=pk).first()
        if not course:
            return {'message': 'Course not found'}, 404
        return course.students

    @marshal_with(courseFields)
    def post(self, pk):
        data = request.json
        student_id = data.get('student_id')
        course = CourseModel.query.filter_by(id=pk).first()
        student = StudentModel.query.filter_by(id=student_id).first()
        if not course or not student:
            return {'message': 'Course or student not found'}, 404
        if student in course.students:
            return {'message': 'Student already enrolled in course'}, 409
        course.students.append(student)
        db.session.commit()
        return course

    @marshal_with(courseFields)
    def delete(self, pk):
        data = request.json
        student_id = data.get('student_id')
        course = CourseModel.query.filter_by(id=pk).first()
        student = StudentModel.query.filter_by(id=student_id).first()
        if not course or not student:
            return {'message': 'Course or student not found'}, 404
        if student not in course.students:
            return {'message': 'Student not enrolled in course'}, 409
        course.students.remove(student)
        db.session.commit()
        return course


def create_api(app):
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    api_resources = [
        (Students, '/students'),
        (Student, '/students/<int:pk>'),
        (Courses, '/courses'),
        (Course, '/courses/<int:pk>'),
        (Groups, '/groups'),
        (Group, '/groups/<int:pk>'),
        (CourseStudents, '/courses_id/<int:pk>')
    ]

    for res, url in api_resources:
        api.add_resource(res, url)

    app.register_blueprint(api_bp, url_prefix='/api/v1')





