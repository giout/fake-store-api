import os

# obtain a cursor right after executing a select query and return a dictionary with the result (using psycopg2 library)
def parse_query_result(cursor):
    result = []
    fields = [field_name.name for field_name in cursor.description]
    rows = cursor.fetchall()
    for row in rows:
        result.append(dict(zip(fields, row)))
    return result

# read a .sql file and obtain the sql sentence as a string
def read_sql(path):
    base_path = 'src/queries'
    result = ''
    with open(os.path.join(base_path, path), 'r', encoding='utf-8') as file:
        result = file.read()
    return result