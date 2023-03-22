import json
from flask_restful import Api
from flask import jsonify, make_response, config, current_app, Blueprint
from flask_restful import Resource, request, marshal_with, fields
from create_db import db, StudentModel, GroupModel, CourseModel
from dicttoxml import dicttoxml
from flasgger import swag_from


# def get_students(order):
#     with db:
#         if order == 'desc':
#             c_db = StudentModel.select().order_by(StudentModel.id)
#         elif order == 'ask':
#             c_db = StudentModel.select().order_by(StudentModel.id[::-1])
#         students = {}
#         for student in c_db:
#             students[student.id] = [student.id, student.first_name, student.last_name,
#                                      student.id]
#     return students
#
#
# class StudentList(Resource):
#
#     @swag_from('static/student.yml')
#     def get(self):
#
#         lis_format = request.args.get('format', default='json')
#         order = request.args.get('order', default="desc")
#
#         if lis_format or order:
#
#             if order == "desc" or order == "ask":
#                 students = get_students(order)
#             else:
#                 raise ValueError("order != desc or order != ask")
#
#             # get format
#             students_json = json.dumps(students, indent=2)
#             response = make_response(students_json)
#             response.headers["content-type"] = "application/json"
#             if lis_format == 'xml':
#                 students_xml = dicttoxml(students, attr_type=False)
#                 response = make_response(students_xml)
#                 response.headers['content-type'] = 'application/xml'
#             elif lis_format != 'json':
#                 raise ValueError("format != json or xml")
#
#             return response

studentFields = {
    'id':fields.Integer,
    'first_name':fields.String,
    'last_name':fields.String,
    'group_id': fields.Integer
}


courseFields = {
    'id':fields.Integer,
    'name':fields.String,
    'description':fields.String
}

groupeFields = {
    'id':fields.Integer,
    'name':fields.String,
}


class Students(Resource):
    @marshal_with(studentFields)
    def get(self):
        return StudentModel.query.all()

    def post(self):
        data = request.json
        student = StudentModel(
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        db.session.add(student)
        db.session.commit()

        return StudentModel.quary.all()




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

    def delete(self, pk):
        course = CourseModel.query.filter_by(id=pk).first()
        if not course:
            return {'message': 'Course not found'}, 404

        db.session.delete(course)
        db.session.commit()
        return {'message': 'Course deleted'}, 200


def create_api(app):
    api = Api(app)
    api.add_resource(Students, '/students')
    api.add_resource(Student, '/students/<int:pk>')
    api.add_resource(Courses, '/courses')
    api.add_resource(Course, '/courses/<int:pk>')
    api.add_resource(Groups, '/groups')
    api.add_resource(Group, '/groups/<int:pk>')
    api.init_app(app)
    return api
