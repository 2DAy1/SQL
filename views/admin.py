from flask import Blueprint, jsonify
from Py_app import db


admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.cli.command('run')
def server_run():
    ...