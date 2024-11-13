from flask import Flask
from config import PORT
from controllers import category, product, user
from utils import api_error_handler

app = Flask(__name__)

# set routes
app.register_blueprint(category) # /categories
app.register_blueprint(product) # /products 
app.register_blueprint(user) # /users

# error handler
app.register_error_handler(Exception, api_error_handler)

if __name__ == '__main__':
    app.run(debug=True, port=PORT)