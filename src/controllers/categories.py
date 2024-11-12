from flask import Blueprint, request, Response
from services import categories
from utils import param_type

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