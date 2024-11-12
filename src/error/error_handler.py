from error import APIException
from marshmallow import ValidationError

# all errors will be handled with APIException, but it a non-APIException exception occurs, it will be returned a 400 error by default
def api_error_handler(error):
    if isinstance(error, APIException):
        return {
            "status_code": error.status_code,
            "message": error.message
        }
    else:
        return {
            "status_code": 400,
            "message": error.args
        }        