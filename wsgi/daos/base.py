
from conn import DbConnection
import cerberus
import utils
from utils.exceptions import CerberusValidationException


class Base():


    def __init__(
        self):

        self.collection = DbConnection.get_db_instance()[self.collection_name]
        self.validator = cerberus.Validator(self.collection_schema)


    def insert_one(self, data):

        if not self.validator.validate(data):
            raise CerberusValidationException(self.validator.errors)

        return self.collection.insert_one(data).inserted_id


    def get_many(self, filters={}):

        return self.collection.find(filters)
