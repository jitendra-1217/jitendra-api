
from conn import client, db

class Base():

    def __init__(self):
        self.collection = None
        self.db = db


    def insert_one(self, data):
        return self.collection.insert_one(data).inserted_id
