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


def get_user_by_email(email):
    query = db.read_sql(base_path+'get-user-by-email.sql')
    return db.execute_query(query, (email,))
        

def create_user(payload):
    # verify email does not exist
    user_with_email = get_user_by_email(payload['email'])
    if len(user_with_email) > 0:
        raise APIException('Email already exists', 400)

    query = db.read_sql(base_path+'create-user.sql')
    return db.execute_query(query, (
        payload['name'],
        payload['email'],
        payload['image_url'],
        hasher.hash(payload['password'],) # encrypt password
    ))


def update_user(id, payload):
    # verify if user exists
    user_with_id = get_user_by_id(id)
    if (len(user_with_id) == 0):
        raise APIException(f'User with id {id} does not exist', 404)

    # if attribute is not present in payload, use existing value
    name = payload.get('name', user_with_id[0]['name'])
    image_url = payload.get('image_url', user_with_id[0]['image_url'])
    email = payload.get('email', user_with_id[0]['email'])

    # verify if email is unique
    query = db.read_sql(base_path+'verify-user-email.sql')
    users_found = db.execute_query(query, (email, id,))
    if (len(users_found) > 0):
        raise APIException(f'Email {email} already exists', 400)

    if 'password' in payload:
        query = db.read_sql(base_path+'update-password.sql')
        db.execute_query(query, (hasher.hash(payload['password']),id,))

    query = db.read_sql(base_path+'update-user.sql')
    return db.execute_query(query, (
        name,
        email,
        image_url,
        id
    ))


def delete_user(id):
    # verify if user exists
    user_with_id = get_user_by_id(id)
    if (len(user_with_id) == 0):
        raise APIException(f'User with id {id} does not exist', 404)
    
    query = db.read_sql(base_path+'delete-user.sql')
    return db.execute_query(query, (id,))


def login(payload):
    # verify email exists
    user_with_email = get_user_by_email(payload['email'])
    if len(user_with_email) <= 0:
        raise APIException('User does not exist', 400)
    # verify password is right
    if not hasher.verify(payload['password'], user_with_email[0]['password']):
        raise APIException('Password is incorrect', 400)
    return user_with_email[0]