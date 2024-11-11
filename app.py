from flask import Flask
from config import PORT

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=PORT)