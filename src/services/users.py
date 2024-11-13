from db.connection import db
from utils import APIException
from passlib.hash import pbkdf2_sha256 as hasher

base_path = 'src/db/queries/user/'

def get_all_users(limit, offset):
    query = db.read_sql(base_path+'get-all-users.sql')
    return db.execute_query(query, (limit, offset,))


def get_user_by_id(id):
    query = db.read_sql(base_path+'get-user-by-id.sql')
    return db.execute_query(query, (id,))


def create_user(payload):
    # verify email does not exist
    query = db.read_sql(base_path+'get-user-by-email.sql')
    users_found = db.execute_query(query, (payload['email'],))
    if len(users_found) > 0:
        raise APIException('Email already exists', 400)

    query = db.read_sql(base_path+'create-user.sql')
    return db.execute_query(query, (
        payload['name'],
        payload['email'],
        payload['image_url'],
        hasher.hash(payload['password'],) # encrypt password
    ))

