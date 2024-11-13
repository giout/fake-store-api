from db.connection import db

db.execute_query(db.read_sql('src/db/queries/ddl.sql'))