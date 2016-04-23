
from flask import Response
import json


def make(
    response,
    status_code=200):

    return Response(
        json.dumps(
            {
                'response': response}),
        mimetype='application/json',
        status=status_code)
