'''
Daily logs -  endpoints
'''


from flask import Blueprint, request
daily_log_bp = Blueprint('daily_log', __name__)

from myflaskapp import basic_auth

from utils import response
from utils.exceptions import CerberusValidationException, ExceptionCodes, ExceptionMessages

from daos.daily_log import DailyLog
dao = DailyLog()


# ------------------------------------------------------------
# None authenticated routes


@daily_log_bp.route('/public', methods=['GET'])
def list_public():

    return _list(
        filters={'is_private': False})


# ------------------------------------------------------------
# Authenticated routes


@daily_log_bp.route('/', methods=['POST'])
@basic_auth.required
def post():

    try:
        return response.make(dao.insert_one(request.get_json()))
    except CerberusValidationException as e:
        return response.make(e.errors(), ExceptionCodes.HTTP_BAD_ATTRIBUTE_ERROR)


@daily_log_bp.route('/all', methods=['GET'])
@basic_auth.required
def list_all():

    return _list()


# ------------------------------------------------------------
# None route functions
#   - To be used only in this file


def _list(
    filters={}):

    return response.make(dao.get_many(filters=filters))
