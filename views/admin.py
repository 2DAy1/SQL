from flask import Blueprint, jsonify
from Py_app import db


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/groups')
def get_groups():
    groups = db.Group.query.all()
    return jsonify([group.to_dict() for group in groups])

@admin.route('/courses')
def get_courses():
    courses = db.Course.query.all()
    return jsonify([course.to_dict() for course in courses])


@admin.route('/students')
def get_students():
    students = db.Student.query.all()
    return jsonify([student.to_dict() for student in students])
