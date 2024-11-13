from utils import APIException
from flask import Response
import json

# all errors will be handled with APIException, but it a non-APIException exception occurs, it will be returned a 400 error by default
def api_error_handler(error):
    if isinstance(error, APIException):
        res = {"message": error.message}
        code = error.status_code
    else:
        res = {"message": error.args}
        code = 400

    return Response(
        response=json.dumps(res), 
        status=code, 
        content_type=json
    )        