# Complete these classes


class OK:
    
    def __init__(self) -> None:
        self.error_code = 200
        self.error_message = 'OK'
    
    def status(self, error_object):
        if error_object == self.error_code:
            return f'message: {self.error_message}: {self.error_code}'


class NotFound(OK):
    def __init__(self) -> None:
        self.error_code = 404
        self.error_message = "This page does not exist"
    
    def status(self, error_object):
        if error_object == self.error_code:
            return f'error: {self.error_message }: {self.error_code}'


class ServerError(OK):
    def __init__(self) -> None:
        self.error_code = 500
        self.error_message = "Internal Server Error"
    
    def status(self, error_object):
        if error_object == self.error_code:
            return f'error: {self.error_message }: {self.error_code}'