
from myflaskapp import app
import pymongo


class DbConnection():

    # Class members
    db = None


    @classmethod
    def get_db_instance(
        cls):

        if not cls.db:
            client = pymongo.MongoClient(app.config['MONGO_URI'])
            cls.db = client[app.config['MONGO_DBNAME']]

        return cls.db
