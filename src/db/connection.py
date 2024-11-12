import psycopg2
from config import DB_URI

connection = psycopg2.connect(DB_URI)