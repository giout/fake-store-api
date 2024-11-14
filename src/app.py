from flask import Flask
from config import PORT, JWT_SECRET
from controllers import category, product, user, auth
from utils import api_error_handler
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# jwt settings
app.config['JWT_SECRET_KEY'] = JWT_SECRET
jwt = JWTManager(app)

# set routes
app.register_blueprint(category) # /categories
app.register_blueprint(product) # /products 
app.register_blueprint(user) # /users
app.register_blueprint(auth) # /auth

# error handler
app.register_error_handler(Exception, api_error_handler)

if __name__ == '__main__':
    app.run(debug=True, port=PORT)