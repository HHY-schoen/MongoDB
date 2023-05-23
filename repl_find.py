import pymongo
from pprint import pprint 

hosts = ['localhost:20000','localhost:20000','localhost:20002']
client = pymongo.MongoClient(hosts)

db = client.test
docs = db.test.find()
print(list(docs))