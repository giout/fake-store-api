from flask import Blueprint, request, jsonify
from services import products
from dto import UrlSchema, CreateCategorySchema

# /products
product = Blueprint('product', __name__, url_prefix='/products')

# GET /products
@product.route('/')
def get_all_products():
    data = products.get_all_products(
        price_min=request.args.get('price_min', default=None, type=float),
        price_max=request.args.get('price_max', default=None, type=float),
        name=request.args.get('name', default='', type=str),
        limit=request.args.get('limit', default=10, type=int),
        offset=request.args.get('offset', default=0, type=int)
    )
    return jsonify({ 
        "data": data, 
        "limit": request.args.get('limit', default=10, type=int), 
        "offset": request.args.get('offset', default=0, type=int) 
    })


# GET /products/<id>
@product.route('/<id>')
def get_product_by_id(id):
    UrlSchema().load({ "id": id }) # validate path id
    data = products.get_product_by_id(id)
    return jsonify({ "data": data })


# POST /products
@product.route('/', methods=['POST'])
def create_product():
    CreateCategorySchema().load(request.json) # validate body
    data = products.create_product(request.json)
    return jsonify({ "data": data }), 201


@product.route('/<id>', methods=['PUT'])
def update_product(id):
    UrlSchema().load({ "id": id }) # validate path id
    CreateCategorySchema().load(request.json, partial=True) # validate body
    products.update_product(id, request.json)
    return jsonify({})


@product.route('/<id>', methods=['DELETE'])
def delete_product(id):
    UrlSchema().load({ "id": id }) # validate path id
    products.delete_product(id)
    return jsonify({})