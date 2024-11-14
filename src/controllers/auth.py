from flask import Blueprint, jsonify, request
from services import users
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from utils import APIException

# /auth
auth = Blueprint('auth', __name__, url_prefix='/auth')

# POST /auth/login
@auth.route('/login', methods=['POST'])
def login():
    user = users.login(request.json)
    return jsonify({ "token": create_access_token(identity=user['id']) }), 201


# GET /auth/user
@auth.route('/user')
@jwt_required()
def get_auth_user():
    user_id = get_jwt_identity()
    user = users.get_user_by_id(user_id)
    if (len(user) <= 0):
        raise APIException('User does not exist', 404)
    return jsonify({ "user": user[0] })