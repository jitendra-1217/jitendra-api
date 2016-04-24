
from conn import client, db
import cerberus
import utils
from utils.exceptions import CerberusValidationException

class Base():

    def __init__(
        self,
        collection_name,
        collection_schema):

        self.db = db
        self.collection = self.db[collection_name]
        self.validator = cerberus.Validator(collection_schema)


    def insert_one(self, data):
        if not self.validator.validate(data):
            raise CerberusValidationException(self.validator.errors)

        return self.collection.insert_one(data).inserted_id
