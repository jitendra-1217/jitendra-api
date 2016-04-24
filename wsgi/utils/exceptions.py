
import ast

class CerberusValidationException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

    def errors(self):
        return ast.literal_eval(str(self))
