from dotenv import load_dotenv, find_dotenv
from os import environ as env

### Load the .env file
load_dotenv(find_dotenv())

PORT=env['PORT']
DB_URI=env['DB_URI']
JWT_SECRET=env['JWT_SECRET']