from db.connection import db
from services import categories
from utils import APIException

base_path = 'src/db/queries/product/'

def get_all_products(price_min, price_max, name, limit, offset):
    query = db.read_sql(base_path+'get-all-products.sql')
    return db.execute_query(query, (name, price_min, price_max, limit, offset,))


def get_products_by_category(id, limit, offset):
    # verify if category exists
    category_with_id = categories.get_category_by_id(id)
    if (len(category_with_id) == 0):
        raise APIException(f'Category with id {id} does not exist', 400)
    
    query = db.read_sql(base_path+'get-products-by-category.sql')
    return db.execute_query(query, (id, limit, offset,))


def get_product_by_id(id): 
    query = db.read_sql(base_path+'get-product-by-id.sql')
    return db.execute_query(query, (id,))