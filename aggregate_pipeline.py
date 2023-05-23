import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.opendata

pipeline = []

docs = db.AQI.aggregate(pipeline)
pprint(list(docs))
