
from flask import Blueprint, request
daily_log_bp = Blueprint('daily_log', __name__)

from myflaskapp import basic_auth

from utils import response
from utils.exceptions import CerberusValidationException

from daos.daily_log import DailyLog
collection = DailyLog()


@daily_log_bp.route('/', methods=['POST'])
@basic_auth.required
def post():
    try:
        return response.make(collection.insert_one(request.get_json()))
    except CerberusValidationException as e:
        return response.make(e.errors(), 400)


@daily_log_bp.route('/public', methods=['GET'])
def get_public():
    pass

@daily_log_bp.route('/all', methods=['GET'])
def get_all():
    pass
