from flask import Blueprint, request
from services import categories
from utils import param_type
from dto import UrlSchema, CreateCategorySchema

# /categories
category = Blueprint('category', __name__, url_prefix='/categories')

# GET /categories
@category.route('/')
def get_all_categories():
    args = request.args #query parameters
    limit = args.get('limit') if param_type(args.get('limit'), int) else 10
    offset = args.get('offset') if param_type(args.get('offset'), int) else 0

    return {
        "data": categories.get_all_categories(
            limit=limit,
            offset=offset
        ),
        "limit": limit,
        "offset": offset
    } 

# GET /categories/<id>
@category.route('/<id>')
def get_category_by_id(id):
    UrlSchema().load({ "id": id }) #verify id is valid
    return {
        "data": categories.get_category_by_id(id) 
    }

# POST /categories
@category.route('/', methods=['POST'])
def create_category():
    body = request.json
    CreateCategorySchema().load(body)
    category = categories.create_category(body)
    return {
        "data": category
    }