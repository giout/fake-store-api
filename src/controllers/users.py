from flask import Blueprint, request, jsonify
from services import users

# /user
user = Blueprint('user', __name__, url_prefix='/users')

# GET /users
@user.route('/')
def get_all_users():
    data = users.get_all_users(
        limit=request.args.get('limit', default=10, type=int),
        offset=request.args.get('offset', default=0, type=int)
    )
    return jsonify({
        "data": data,
        "limit": request.args.get('limit', default=10, type=int),
        "offset": request.args.get('offset', default=0, type=int)
    })