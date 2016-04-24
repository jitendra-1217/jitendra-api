
from flask import Response
from bson.json_util import dumps


def make(
    response,
    status_code=200):

    return Response(
        dumps(
            {
                'response': response}),
        mimetype='application/json',
        status=status_code)
