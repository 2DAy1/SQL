import json
from flask_restful import Api
from flask import jsonify, make_response, config, current_app, Blueprint
from flask_restful import Resource, request
from Py_app import db, Student
from dicttoxml import dicttoxml
from flasgger import swag_from




def get_students(order):
    with db:
        if order == 'desc':
            c_db = Student.select().order_by(Student.id)
        elif order == 'ask':
            c_db = Student.select().order_by(Student.id[::-1])
        students = {}
        for students in c_db:
            students[students.id] = [students.id, students.first_name, students.last_name,
                                     students.id]
    return students


class StudentList(Resource):

    @swag_from('static/student.yml')
    def get(self):

        lis_format = request.args.get('format', default='json')
        order = request.args.get('order', default="desc")

        if lis_format or order:

            if order == "desc" or order == "ask":
                students = get_students(order)
            else:
                raise ValueError("order != desc or order != ask")

            # get format
            students_json = json.dumps(students, indent=2)
            response = make_response(students_json)
            response.headers["content-type"] = "application/json"
            if lis_format == 'xml':
                students_xml = dicttoxml(students, attr_type=False)
                response = make_response(students_xml)
                response.headers['content-type'] = 'application/xml'
            elif lis_format != 'json':
                raise ValueError("format != json or xml")

            return response


def create_api(app):
    api = Api(app)
    api.add_resource(StudentList, '/api/v1/report/')
    api.init_app(app)
    return api
