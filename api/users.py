from flask import Blueprint, jsonify, request
from models.users_models import users

# define the blueprint
blueprint_users = Blueprint(name="blueprint_users", import_name=__name__)

@blueprint_users.route('/index', methods=['GET'])
def index():
    row = users.index()
    return jsonify(row)

@blueprint_users.route('/detail/<int : id>', methods=['GET'])
def detail(id):
    row = users.detail(id)
    return jsonify(row)
