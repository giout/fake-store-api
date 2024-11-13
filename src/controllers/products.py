from flask import Blueprint, request, jsonify
from services import products
from dto import UrlSchema

# /categories
product = Blueprint('product', __name__, url_prefix='/products')

# GET /products
@product.route('/')
def get_all_products():
    #query parameters
    args = request.args  
    data = products.get_all_products(
        price_min=args.get('price_min', default=None, type=float),
        price_max=args.get('price_max', default=None, type=float),
        name=args.get('name', default='', type=str),
        limit=args.get('limit', default=10, type=int),
        offset=args.get('offset', default=0, type=int)
    )
    return jsonify({ 
        "data": data, 
        "limit": args.get('limit', default=10, type=int), 
        "offset": args.get('offset', default=0, type=int) 
    })


# GET /products/<id>
@product.route('/<id>')
def get_category_by_id(id):
    UrlSchema().load({ "id": id }) # validate path id
    data = products.get_product_by_id(id)
    return jsonify({ "data": data })