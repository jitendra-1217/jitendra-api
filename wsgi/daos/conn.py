
from myflaskapp import app
import pymongo

client = pymongo.MongoClient(app.config['MONGO_URI'])
db = client[app.config['MONGO_DBNAME']]
