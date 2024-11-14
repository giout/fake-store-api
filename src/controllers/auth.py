from flask import Blueprint, jsonify, request
from services import users
from flask_jwt_extended import create_access_token

# /auth
auth = Blueprint('auth', __name__, url_prefix='/auth')

# POST /auth/login
@auth.route('/login', methods=['POST'])
def login():
    user = users.login(request.json)
    return jsonify({ "token": create_access_token(identity=user['id']) })