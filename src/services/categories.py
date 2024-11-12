from db import connection, parse_query_result, read_sql

def get_all_categories(limit, offset):
    with connection as cnn:
        with cnn.cursor() as cursor:
            cursor.execute(
                read_sql('category/get-all-categories.sql'), 
                (limit, offset)
            )
            return parse_query_result(cursor)
        

def get_category_by_id(id): 
    with connection as cnn:
        with cnn.cursor() as cursor:
            cursor.execute(
                read_sql('category/get-category-by-id.sql'), 
                (id,)  
            )
            return parse_query_result(cursor)