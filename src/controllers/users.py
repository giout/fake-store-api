from flask import Blueprint, request, jsonify
from services import users
from dto import UrlSchema

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


# GET /users/<id>
@user.route('/<id>')
def get_user_by_id(id):
    UrlSchema().load({ "id": id }) # validate path id
    data = users.get_user_by_id(id)
    return jsonify({ "data": data })