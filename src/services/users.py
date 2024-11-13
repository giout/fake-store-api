from db.connection import db

base_path = 'src/db/queries/user/'

def get_all_users(limit, offset):
    query = db.read_sql(base_path+'get-all-users.sql')
    return db.execute_query(query, (limit, offset,))