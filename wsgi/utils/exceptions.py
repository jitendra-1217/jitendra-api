
# ------------------------------------------------------------
# Exception codes
class ExceptionCodes():

    HTTP_INTERNAL_SERVER_ERROR = 500
    HTTP_BAD_ATTRIBUTE_ERROR   = 400


# ------------------------------------------------------------
# Exception messages
class ExceptionMessages():

    INTERNAL_SERVER_ERROR = 'Internal server error!'


# ------------------------------------------------------------
# Custom exception classes

import ast

class CerberusValidationException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

    def errors(self):
        return ast.literal_eval(str(self))
