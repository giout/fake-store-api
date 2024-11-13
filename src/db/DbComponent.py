import psycopg2 

class DbComponent():
    def __init__(self, DB_URI):
        self.connection = psycopg2.connect(DB_URI)


    def execute_query(self, query, params=None):
        with self.connection as cnn:
            with cnn.cursor() as cursor:
                cursor.execute(query, params)
                return self.__parse_query_result(cursor)
    

    # read a .sql file and obtain the sql sentence as a string
    def read_sql(self, path: str):
        result = ''
        with open(path, 'r', encoding='utf-8') as file:
            result = file.read()
        return result


    # obtain a cursor right after executing a select query and return a dictionary with the result (using psycopg2 library)
    def __parse_query_result(self, cursor):
        result = []
        if cursor.description is not None: # if sql query returns values
            fields = [field_name.name for field_name in cursor.description]
            rows = cursor.fetchall()
            for row in rows:
                result.append(dict(zip(fields, row)))
        return result