from db import connection, read_sql

with connection as cnn:
    with connection.cursor() as cursor:
        cursor.execute(read_sql('ddl.sql'))