from db.connection import db
from utils import APIException

base_path = 'src/db/queries/category/'

def get_all_categories(limit, offset):
    query = db.read_sql(base_path+'get-all-categories.sql')
    return db.execute_query(query, (limit, offset,))


def get_category_by_id(id): 
    query = db.read_sql(base_path+'get-category-by-id.sql')
    return db.execute_query(query, (id,))


def create_category(payload):
    # verify if there is a category with the same name
    query = db.read_sql(base_path+'get-category-by-name.sql')
    categories_found = db.execute_query(query, (payload['name'], ))
    if (len(categories_found) > 0):
        raise APIException(f'Category {payload["name"]} already exists', 400)

    # if category does not exist, create it
    query = db.read_sql(base_path+'create-category.sql')
    return db.execute_query(query, (payload['name'], payload['image_url'],))


def update_category(id, payload):
    # verify if category exists
    category_with_id = get_category_by_id(id)
    if (len(category_with_id) == 0):
        raise APIException(f'Category with id {id} does not exist', 400)

    # if name will be updated, verify if there is a category with the same name
    if 'name' in payload:
        query = db.read_sql(base_path+'get-category-by-name.sql')
        categories_found = db.execute_query(query, (payload['name'],))
        if (len(categories_found) > 0):
            raise APIException(
                f'Category {payload["name"]} already exists', 
                400
            )
    
    # if attribute is not present in payload, use existing value
    name = payload.get('name', category_with_id[0]['name'])
    image_url = payload.get('image_url', category_with_id[0]['image_url'])

    query = db.read_sql(base_path+'update-category.sql')
    return db.execute_query(query, (name, image_url, id,))


def delete_category(id):
    # verify if category exists
    category_with_id = get_category_by_id(id)
    if (len(category_with_id) == 0):
        raise APIException(f'Category with id {id} does not exist', 400)

    query = db.read_sql(base_path+'delete-category.sql')
    return db.execute_query(query, (id,))