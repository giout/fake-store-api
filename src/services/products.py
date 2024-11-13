from db.connection import db

base_path = 'src/db/queries/product/'

def get_all_products(price_min, price_max, name, limit, offset):
    query = db.read_sql(base_path+'get-all-products.sql')
    return db.execute_query(query, (name, price_min, price_max, limit, offset,))