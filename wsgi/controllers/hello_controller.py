'''
This controller is for testing purposes
'''


from flask import Blueprint
hello_bp = Blueprint('hello', __name__)

from myflaskapp import basic_auth

from utils import response


@hello_bp.route('/')
def index():
    return response.make('Hello!')


@hello_bp.route('/secret')
@basic_auth.required
def index_secret():
    return response.make('Hello secret!')
