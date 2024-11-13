class APIException(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        # 400 is status code by default
        self.status_code = status_code if status_code else 400 

    def __str__(self):
        return self.message