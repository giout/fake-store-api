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
        raise APIException(f'Category with id {id} does not exist', 404)
    
    query = db.read_sql(base_path+'get-products-by-category.sql')
    return db.execute_query(query, (id, limit, offset,))


def get_product_by_id(id): 
    query = db.read_sql(base_path+'get-product-by-id.sql')
    return db.execute_query(query, (id,))


def create_product(payload):
    # verify if there is a product with the same name
    query = db.read_sql(base_path+'get-product-by-name.sql')
    products_found = db.execute_query(query, (payload['name'], ))
    if (len(products_found) > 0):
        raise APIException(f'Product {payload["name"]} already exists', 400)

    # verify if category exists
    category_with_id = categories.get_category_by_id(payload["category"])
    if (len(category_with_id) == 0):
        raise APIException(f'Category with id {payload["category"]} does not exist', 400)

    # if product does not exist and category does exist, create product
    query = db.read_sql(base_path+'create-product.sql')
    return db.execute_query(query, (
        payload['name'], 
        payload['image_url'],
        payload['price'],
        payload['description'],
        payload['category'],
    ))


def update_product(id, payload):
    # verify if product exists
    product_with_id = get_product_by_id(id)
    if len(product_with_id) == 0:
        raise APIException(f'Product with id {id} does not exist', 404)

    # assign attributes that are not present in payload
    name = payload.get('name', product_with_id[0]['name'])
    image_url = payload.get('image_url', product_with_id[0]['image_url'])
    description = payload.get('description', product_with_id[0]['description'])
    price = payload.get('price', product_with_id[0]['price'])
    category = payload.get('category_id', product_with_id[0]['category_id'])

    # verify if category exists
    category_with_id = categories.get_category_by_id(id)
    if (len(category_with_id) == 0):
        raise APIException(f'Category with id {id} does not exist', 400)

    # verify if name is unique
    query = db.read_sql(base_path+'verify-product-name.sql')
    products_found = db.execute_query(query, (name, id,))
    if (len(products_found) > 0):
        raise APIException(f'Product {name} already exists', 400)
    
    query = db.read_sql(base_path+'update-product.sql')
    return db.execute_query(query,(name, description, category, image_url, price, id,))


def delete_product(id):
    # verify if product exists
    product_with_id = get_product_by_id(id)
    if len(product_with_id) == 0:
        raise APIException(f'Product with id {id} does not exist', 404)
    
    query = db.read_sql(base_path+'delete-product.sql')
    return db.execute_query(query,(id,))