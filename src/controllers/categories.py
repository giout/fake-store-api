from flask import Blueprint, request, Response
from services import categories
from utils import param_type
from dto import UrlSchema, CreateCategorySchema
import json

# /categories
category = Blueprint('category', __name__, url_prefix='/categories')

# GET /categories
@category.route('/')
def get_all_categories():
    args = request.args #query parameters
    limit = args.get('limit') if param_type(args.get('limit'), int) else 10
    offset = args.get('offset') if param_type(args.get('offset'), int) else 0

    res = {
        "data": categories.get_all_categories(
            limit=limit,
            offset=offset
        ),
        "limit": limit,
        "offset": offset
    } 

    return Response(status=200, response=json.dumps(res), content_type=json)


# GET /categories/<id>
@category.route('/<id>')
def get_category_by_id(id):
    UrlSchema().load({ "id": id }) #verify id is valid
    res = {
        "data": categories.get_category_by_id(id) 
    }

    return Response(status=200, response=json.dumps(res), content_type=json)


# POST /categories
@category.route('/', methods=['POST'])
def create_category():
    body = request.json
    CreateCategorySchema().load(body)
    category = categories.create_category(body)
    res = {
        "data": category
    }

    return Response(status=201, response=json.dumps(res), content_type=json)


# PUT /categories/<id>
@category.route('/<id>', methods=['PUT'])
def update_category(id):
    body = request.json
    UrlSchema().load({"id": id})
    CreateCategorySchema().load(body, partial=True)
    categories.update_category(id, body)

    return Response(status=200)


# DELETE /categories/<id>
@category.route('/<id>', methods=['DELETE'])
def delete_category(id):
    UrlSchema().load({"id": id})
    categories.delete_category(id)
    
    return Response(status=200)