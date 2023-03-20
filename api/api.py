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
        return StudentModel.query.filter_by(id=pk).first()


class Groups(Resource):
    @marshal_with(groupeFields)
    def get(self):
        return GroupModel.query.all()


class Group(Resource):
    @marshal_with(groupeFields)
    def get(self, pk):
        return GroupModel.query.filter_by(id=pk).first()


class Courses(Resource):
    @marshal_with(courseFields)
    def get(self):
        return CourseModel.query.all()


class Course(Resource):
    @marshal_with(courseFields)
    def get(self, pk):
        return CourseModel.query.filter_by(id=pk).first()


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
