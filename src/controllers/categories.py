from flask import Blueprint, request, jsonify
from services import categories, products
from dto import UrlSchema, CreateCategorySchema

# /categories
category = Blueprint('category', __name__, url_prefix='/categories')

# GET /categories
@category.route('/')
def get_all_categories():
    #query parameters
    data = categories.get_all_categories(
        limit=request.args.get('limit', default=10, type=int), 
        offset=request.args.get('offset', default=0, type=int)
    )
    return jsonify({ 
        "data": data, 
        "limit": request.args.get('limit', default=10, type=int), 
        "offset": request.args.get('offset', default=0, type=int) 
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
    CreateCategorySchema().load(request.json) # validate body
    data = categories.create_category(request.json)
    return jsonify({ "data": data }), 201


# PUT /categories/<id>
@category.route('/<id>', methods=['PUT'])
def update_category(id):
    UrlSchema().load({"id": id}) # validate id
    CreateCategorySchema().load(request.json, partial=True) # validate body
    categories.update_category(id, request.json)
    return jsonify({})


# DELETE /categories/<id>
@category.route('/<id>', methods=['DELETE'])
def delete_category(id):
    UrlSchema().load({"id": id}) # validate id
    categories.delete_category(id)
    return jsonify({})


# GET /categories/<id>/products
@category.route('/<id>/products')
def get_products_by_category(id):
    UrlSchema().load({"id": id}) # validate id
    data = products.get_products_by_category(
        id,
        limit=request.args.get('limit', default=10, type=int),
        offset=request.args.get('offset', default=0, type=int)
    )
    return jsonify({
        "data": data,
        "limit": request.args.get('limit', default=10, type=int),
        "offset": request.args.get('offset', default=0, type=int),
    })