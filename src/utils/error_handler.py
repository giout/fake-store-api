from utils import APIException
from flask import jsonify
import traceback
from werkzeug import exceptions

# all errors will be handled with APIException, but it a non-APIException exception occurs, it will be returned a 400 error by default
def api_error_handler(error: Exception):
    print(traceback.format_exc())
    if isinstance(error, APIException):
        return jsonify({"message": error.message}), error.status_code
    if isinstance(error, exceptions.NotFound):
        return jsonify({"message": 'Endpoint not found' }), 404
    if isinstance(error, exceptions.MethodNotAllowed):
        return jsonify({"message": 'This HTTP method is not allowed for the requested URL' }), 400
    else:
        return jsonify({"message": error.args}), 500