from dbm import dumb
from flask import Blueprint, jsonify, request
from models.users_models import users
from validate.users_validate import RegisterForm
from flask_wtf import CSRFProtect

csrf = CSRFProtect()
# define the blueprint
blueprint_users = Blueprint(name="blueprint_users", import_name=__name__)

action = users

@blueprint_users.route('/index', methods=['GET'])
def index():
    row = action.index()
    return jsonify(row)

@blueprint_users.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    row = action.detail(id)
    return jsonify(row)

@blueprint_users.route('/save', methods=['POST'])
def save():
    form = RegisterForm()
    password = form.password.data
    name = form.name.data
    email = form.email.data
    if form.validate_on_submit():
        user = action.check_email(email)
        if user is None:
            row = action.store(name,email,password)
            return jsonify(row)
        else:
            return jsonify(status=False,code=500,message="email already exist")
    else:
        err=''
        for error in form.errors:
            err += error

        return jsonify(status=False,code=500,message=err)
