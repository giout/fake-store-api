from flask import Blueprint, request, jsonify
from services import categories
from dto import UrlSchema, CreateCategorySchema

# /categories
category = Blueprint('category', __name__, url_prefix='/categories')

# GET /categories
@category.route('/')
def get_all_categories():
    #query parameters
    args = request.args 
    data = categories.get_all_categories(
        limit=args.get('limit', default=10, type=int), 
        offset=args.get('offset', default=0, type=int)
    )
    return jsonify({ 
        "data": data, 
        "limit": args.get('limit', default=10, type=int), 
        "offset": args.get('offset', default=0, type=int) 
    })


# GET /categories/<id>
@category.route('/<id>')
def get_category_by_id(id):
    UrlSchema().load({ "id": id }) # validate path id
    data = categories.get_category_by_id(id)
    return jsonify({ "data": data })


# POST /categories
@category.route('/', methods=['POST'])
def create_category():
    body = request.json
    CreateCategorySchema().load(body) # validate request body
    data = categories.create_category(body)
    return jsonify({ "data": data }), 201


# PUT /categories/<id>
@category.route('/<id>', methods=['PUT'])
def update_category(id):
    body = request.json
    UrlSchema().load({"id": id}) # validate id
    CreateCategorySchema().load(body, partial=True) # validate request body
    categories.update_category(id, body)
    return jsonify({})


# DELETE /categories/<id>
@category.route('/<id>', methods=['DELETE'])
def delete_category(id):
    UrlSchema().load({"id": id}) # validate id
    categories.delete_category(id)
    return jsonify({})
